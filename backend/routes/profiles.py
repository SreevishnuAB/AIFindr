from fastapi import APIRouter, HTTPException

from handlers.profile import ProfileHandler
from models.profile import PartialProfile, Profile



router = APIRouter(prefix="/profiles")

@router.post("")
def create_profile(profile: Profile) -> Profile:
    """
    Create a new profile.
    """
    ProfileHandler().upsert(profile.id, profile.name, profile.profile_text)
    return profile 


@router.patch("/{profile_id}")
def update_profile(profile_id: str, profile: PartialProfile):
    """
    Update an existing profile.
    """
    
    ProfileHandler().upsert(profile_id, profile.name, profile.profile_text)
    return {"message": "Profile updated successfully"}

@router.get("/{profile_id}")
def get_profile(profile_id: str) -> Profile:
    """
    Get a profile by ID.
    """
    try:
        return ProfileHandler().fetch(profile_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
