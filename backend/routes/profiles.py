from backend.handlers.profile import ProfileHandler
from backend.models.profile import PartialProfile, Profile
from fastapi import APIRouter

router = APIRouter(prefix="/profiles")

@router.post("")
def create_profile(profile: Profile):
    """
    Create a new profile.
    """
    ProfileHandler().upsert_profile(profile.id, profile.name, profile.profile_text)
    return {"message": "Profile created successfully"} 


@router.patch("/{profile_id}")
def update_profile(profile_id: str, profile: PartialProfile):
    """
    Update an existing profile.
    """
    
    ProfileHandler().upsert_profile(profile_id, profile.name, profile.profile_text)
    return {"message": "Profile updated successfully"}

