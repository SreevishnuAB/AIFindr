from pydantic import BaseModel



class GetCompatibiityReasoningRequest(BaseModel):
    query: str
    profile_text: str