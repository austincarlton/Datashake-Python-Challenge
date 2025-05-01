from fastapi import Header, HTTPException
from app.models import USERS_DB

async def get_current_user(x_api_key: str = Header(...)):
    if x_api_key not in USERS_DB:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    user = USERS_DB[x_api_key]
    if user["credits"] <= 0:
        raise HTTPException(status_code=402, detail="No credits left")
    
    return x_api_key, user
