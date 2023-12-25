import fastapi

router = fastapi.APIRouter()


#controllers and routes
@router.get("/sessions/{id}")
async def read_session():
    return {"courses":[]}


@router.get("/sessions/{id}content-blocks")
async def read_session_content_blocks():
    return {"courses":[]}

@router.get("/content-blocks/{id}")
async def read__content_blocks():
    return {"courses":[]}
