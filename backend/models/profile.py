from typing import List
from pydantic import BaseModel, Field


class Profile(BaseModel):
    id: str
    name: str
    profile_text: str = Field(max_length=10000)


class Profiles(BaseModel):
    profiles: List[Profile]

class CompatibilityReasoning(BaseModel):
    reason: str

class PartialProfile(BaseModel):
    name: str
    profile_text: str = Field(max_length=10000)