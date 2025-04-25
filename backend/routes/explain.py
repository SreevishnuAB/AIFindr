from backend.models.explain import GetCompatibiityReasoningRequest
from backend.models.profile import CompatibilityReasoning
from backend.utils.llm import LLMUtils
from fastapi import APIRouter

router = APIRouter(prefix="/explain")

@router.post("")
def get_compatibility_reasoning(explain_request: GetCompatibiityReasoningRequest) -> CompatibilityReasoning:
    """
    Explain the match between a profile and a search query.
    """

    res = LLMUtils().get_reasoning(
        query=explain_request.query,
        profile=explain_request.profile_text,
    )
    # Logic to explain the match
    return res
