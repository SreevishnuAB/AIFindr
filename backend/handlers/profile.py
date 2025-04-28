import logging

from typing import List
from models.profile import Profile
from models.search import SearchResult
from persistence.db import PineconeWrapper
from utils.llm import LLMUtils


class ProfileHandler:
    def __init__(self):
        self.pc_wrapper = PineconeWrapper()
        self._logger = logging.getLogger(__name__)

    def upsert(self, id: str, name: str, profile_text: str) -> None:
        """
        Upsert a profile into the database.
        """
        embeddings = LLMUtils().get_embeddings(profile_text)
        record = {"id": id, "values": embeddings, "metadata": {"name": name, "profile_text": profile_text}}
        self.pc_wrapper.upsert(records=[record])


    def search(self, query: str) -> List[SearchResult]:
        """
        Retrieve a profile from the database.
        """
        embeddings = LLMUtils().get_embeddings(query)
        results = self.pc_wrapper.query(vector=embeddings)
        print(results)
        if "matches" in results:
            return [SearchResult(profile=self._convert_to_profile_object(result), score=result["score"] * 100) for result in results["matches"]]
        return []
    
    def fetch(self, id: str) -> Profile:
        """
        Fetch a profile from the database.
        """
        result = self.pc_wrapper.fetch(id)
        try:
            metadata = result.vectors[id]["metadata"]
            profile = {
                "id": id,
                "metadata": metadata
                }
            return self._convert_to_profile_object(profile)
        except KeyError as e:
            print(f"KeyError: {e}")
            raise ValueError(f"Profile with ID {id} not found.")
        
    def _convert_to_profile_object(self, result: dict) -> Profile:
        """
        Convert a result from the database to a Profile object.
        """
        return Profile(
            id=result["id"],
            name=result["metadata"]["name"],
            profileText=result["metadata"]["profile_text"]
        )
    
