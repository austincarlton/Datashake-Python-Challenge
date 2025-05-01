import httpx

BASE_URL = "https://api.frankfurter.app"

async def get_supported_currencies():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/currencies")
        return resp.json()

async def convert_currency(from_currency, to_currency, amount, date=None):
    url = f"{BASE_URL}/{date}" if date else f"{BASE_URL}/latest"
    params = {"from": from_currency, "to": to_currency, "amount": amount}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        data = resp.json()
        return {
            "rate": data["rates"][to_currency],
            "converted": data["rates"][to_currency] * amount,
            "date": data["date"]
        }
