from typing import Optional, List
from fastapi import FastAPI, Path , Query
from pydantic import BaseModel

# Initializing
app = FastAPI( title="FastAPI LMS",
    description="LMS for managing students and courses",
    version="0.0.1",
    contact={
        "name": "Michael",
        "email": "michaelnonso718@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
    },)



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
@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.post("/users")
def create_user(user:User):
    users.append(user)
    return "success"


@app.get("/users/{id}")
async def get_user_by_id(id:int=Path(...,description="The ID of the user you want to retrieve",lt=len(users)),
                         q: str =Query(None, max_length=5)
                         ):
    return {"users":users[id],"query":q}