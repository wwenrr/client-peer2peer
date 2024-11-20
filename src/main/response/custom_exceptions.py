from datetime import datetime
from fastapi.responses import JSONResponse

class CustomError(Exception):
    def __init__(self, message: str, code: int):
        self.message = message  
        self.code = code        
        super().__init__(self.message)  


async def custom_error_handler(request, exc: CustomError):
    timestamp = datetime.now().timestamp()
    current_time = datetime.fromtimestamp(timestamp)
    return JSONResponse(
        status_code=exc.code,  
        content={
            "code": exc.code, 
            "timestamp" : current_time.strftime("%Y-%m-%d %H:%M:%S"), 
            "message": exc.message
        }  
    )