import logging
import os
from typing import Dict, List

from dotenv import load_dotenv

load_dotenv()
from pinecone.grpc import PineconeGRPC, GRPCClientConfig
from pinecone import ServerlessSpec


class PineconeWrapper:
    def __init__(self):
        host = os.environ.get("PINECONE_HOST")
        self._dense_index_name = "dense-index"
        self._pc = PineconeGRPC(
            api_key="pclocal", 
            host=host
            )
        self._logger = logging.getLogger(__name__)    
        self._initialize_pinecone()
        self.index = self._get_index()

    def _initialize_pinecone(self):
        if not self._pc.has_index(self._dense_index_name):  
            dense_index_model = self._pc.create_index(
                name=self._dense_index_name,
                vector_type="dense",
                dimension=3072,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
                deletion_protection="disabled",
                tags={"environment": "development"}
            )
            self._logger.info(f"Created index: {dense_index_model}")

    def _get_index(self):
        dense_index_host = self._pc.describe_index(name=self._dense_index_name).host
        dense_index = self._pc.Index(host=dense_index_host, grpc_config=GRPCClientConfig(secure=False))
        return dense_index

    def upsert(self, records: List[Dict]):
        self._logger.info(f"Upserting {len(records)} records to index {self._dense_index_name}")
        self.index.upsert(
            namespace="aifindr",
            vectors=records,
            )

    def query(self, vector: List[float], top_k: int = 5):
        return self.index.query(vector, top_k=top_k, include_metadata=True, namespace="aifindr")
    
    def fetch(self, id: str):
        self._logger.info(f"Getting record by id {id} from index {self._dense_index_name}")
        return self.index.fetch(ids=[id], namespace="aifindr")