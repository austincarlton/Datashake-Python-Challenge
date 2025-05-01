from fastapi import APIRouter, Request, Depends
from app.schemas import SignupResponse, ConvertRequest, ConvertResponse
from app.utils import generate_api_key
from app.models import USERS_DB, DEFAULT_CREDITS
from app.dependencies import get_current_user
from app.services.currency_service import get_supported_currencies, convert_currency

router = APIRouter()

@router.post("/signup", response_model=SignupResponse)
async def signup():
    api_key = generate_api_key()
    USERS_DB[api_key] = {"credits": DEFAULT_CREDITS}
    return {"api_key": api_key, "credits": DEFAULT_CREDITS}

@router.get("/currencies")
async def list_currencies(x=Depends(get_current_user)):
    key, user = x
    user["credits"] -= 1
    return await get_supported_currencies()

@router.post("/convert", response_model=ConvertResponse)
async def convert(req: ConvertRequest, x=Depends(get_current_user)):
    key, user = x
    user["credits"] -= 1
    result = await convert_currency(
        req.from_currency, req.to_currency, req.amount, req.date
    )
    return {
        "from_currency": req.from_currency,
        "to_currency": req.to_currency,
        "amount": req.amount,
        **result
    }

def register_routes(app):
    app.include_router(router)
