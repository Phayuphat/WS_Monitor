
from fastapi.security import APIKeyHeader
from fastapi import Depends, HTTPException
from starlette import status


# load config from .env to get X-API-KEY list
X_API_KEY = APIKeyHeader(name="X-API-Key")
API_KEY = "YOUR_API_KEY"


def api_key_auth(x_api_key: str = Depends(X_API_KEY)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
