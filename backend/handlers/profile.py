import logging
from typing import List
from backend.models.profile import Profile
from backend.models.search import SearchResult
from backend.persistence.db import PineconeWrapper
from backend.utils.llm import LLMUtils


class ProfileHandler:
    def __init__(self):
        self.pc_wrapper = PineconeWrapper()
        self._logger = logging.getLogger(__name__)

    def upsert_profile(self, id: str, name: str, profile_text: str) -> None:
        """
        Upsert a profile into the database.
        """
        embeddings = LLMUtils().get_embeddings(profile_text)
        record = {"id": id, "values": embeddings, "metadata": {"name": name, "profile_text": profile_text}}
        self.pc_wrapper.upsert(records=[record])


    def search_profiles(self, query: str) -> List[SearchResult]:
        """
        Retrieve a profile from the database.
        """
        embeddings = LLMUtils().get_embeddings(query)
        results = self.pc_wrapper.query(vector=embeddings)
        if "matches" in results:
            return [SearchResult(profile=self._convert_to_profile(result), score=result["score"] * 100) for result in results["matches"]]
        return []
        
    def _convert_to_profile(self, result: dict) -> Profile:
        """
        Convert a result from the database to a Profile object.
        """
        return Profile(
            id=result["id"],
            name=result["metadata"]["name"],
            profile_text=result["metadata"]["profile_text"]
        )
    
