# Currency Converter API

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload
```

## Features
- Signup and receive API key + credits
- Get list of supported currencies
- Convert currencies (with optional historical date)
- Credits deducted per request
- Async implementation

## Docs
Visit: http://localhost:8000/docs
