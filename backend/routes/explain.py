from fastapi import APIRouter

from models.explain import CompatibilityReasoning, GetCompatibiityReasoningRequest
from utils.llm import LLMUtils


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
