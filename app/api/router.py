from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/ping")
async def status_server():
    """
    Check if the server is up.
    :return: a JSONResponse with code 200 if the server is up.
    """
    return JSONResponse(status_code=200, content={"message": "Server is up!"})