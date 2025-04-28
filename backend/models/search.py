from typing import List
from models.profile import Profile
from pydantic import BaseModel

class Search(BaseModel):
    """
    Search model for searching profiles.
    """

    query: str


class SearchResult(BaseModel):
    """
    Search result model for returning search results.
    """

    profile: Profile
    score: float


class SearchResults(BaseModel):
    """
    Search results model for returning multiple search results.
    """

    results: List[SearchResult]