from fastapi import  FastAPI
from src.main.response.custom_exceptions import CustomError, custom_error_handler

from src.main.router.fileRouter import router as fileRouter
from src.main.router.testRouter import router as testRouter

app = FastAPI()

app.add_exception_handler(CustomError, custom_error_handler)
app.include_router(testRouter)
app.include_router(fileRouter)

import uvicorn
port = 8000
uvicorn.run(app, host="0.0.0.0", port = port)