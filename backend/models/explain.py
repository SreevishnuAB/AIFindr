from pydantic import BaseModel, Field



class GetCompatibiityReasoningRequest(BaseModel):
    query: str
    profile_text: str = Field(alias="profileText", max_length=10000)


class CompatibilityReasoning(BaseModel):
    reason: str