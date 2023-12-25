from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users=[
  {
    "email": "string1",
    "is_active": True,
    "bio": "string"
  },
  {
    "email": "string2",
    "is_active": True,
    "bio": "string"
  },
  {
    "email": "string3",
    "is_active": True,
    "bio": "string"
  },
  {
    "email": "string4",
    "is_active": True,
    "bio": "string"
  },
  {
    "email": "string5",
    "is_active": True,
    "bio": "string"
  }
]

# Defining a model
class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

#controllers and routes
@router.get("/users", response_model=List[User])
def get_users():
    return users

@router.post("/users")
def create_user(user:User):
    users.append(user)
    return "success"


@router.get("/users/{id}")
async def get_user_by_id(id:int):
    return users[id]