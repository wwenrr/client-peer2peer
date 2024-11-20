from fastapi.responses import JSONResponse
from datetime import datetime

async def res(msg):
    timestamp = datetime.now().timestamp()
    current_time = datetime.fromtimestamp(timestamp)
    return JSONResponse(
        status_code=200,  
        content = {
            "code": 200, 
            "timestamp" : current_time.strftime("%Y-%m-%d %H:%M:%S"), 
            "response": msg
        }
    )