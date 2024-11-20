from fastapi import APIRouter
from src.main.response.custom_exceptions import CustomError
from src.main.response.httpOk import res

router = APIRouter()

@router.get("/file")
async def api():
    return await res(["super idol", "a", "b", "c"])

print("\033[33mNạp fileRouter thành công\033[0m")
