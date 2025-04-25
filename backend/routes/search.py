from backend.handlers.profile import ProfileHandler
from backend.models.search import Search, SearchResults
from fastapi import APIRouter

router = APIRouter(prefix="/search")


@router.post("")
def search_profiles(search_query: Search):
    """
    Search for a profile.
    """
    results = ProfileHandler().search_profiles(search_query.query)
    # Logic to search for a profile
    return SearchResults(results=results)