from typing import Dict
from uuid import uuid4

# In-memory storage simulation
USERS_DB: Dict[str, Dict] = {}

DEFAULT_CREDITS = 100
RATE_LIMIT_PER_MINUTE = 10
