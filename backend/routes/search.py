from fastapi import APIRouter

from handlers.profile import ProfileHandler
from models.search import Search, SearchResults


router = APIRouter(prefix="/search")


@router.post("")
def search_profiles(search_query: Search):
    """
    Search for a profile.
    """
    results = ProfileHandler().search(search_query.query)
    # Logic to search for a profile
    return SearchResults(results=results)