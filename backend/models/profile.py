from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class PartialProfile(BaseModel):
    name: str
    profile_text: str = Field(max_length=10000, alias="profileText")

class Profile(PartialProfile):
    id: str = Field(default_factory=lambda: str(uuid4().hex))


class Profiles(BaseModel):
    profiles: List[Profile]
