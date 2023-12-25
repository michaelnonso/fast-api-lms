from typing import Optional, List
from fastapi import FastAPI, Path , Query
from pydantic import BaseModel
from api import users,courses,sessions


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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sessions.router)



