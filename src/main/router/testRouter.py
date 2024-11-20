from fastapi import APIRouter
from src.main.response.httpOk import res

router = APIRouter()

@router.get("/")
async def api():
    return await res("Server is alive!")

print("\033[33mNạp testRouter thành công\033[0m")
