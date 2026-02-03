from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
import hashlib

SECRET_KEY = "SECRET"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Truncate password to 72 characters before hashing to avoid bcrypt limit
def _prehash(password: str) -> str:
    # Truncate password to 72 characters before SHA-256 (not after)
    if len(password) > 72:
        password = password[:72]  # Keep only first 72 characters
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def hash_password(password: str):
    prehashed = _prehash(password)  # First truncate then pre-hash
    return pwd_context.hash(prehashed)  # Apply bcrypt

def verify_password(password: str, hashed):
    prehashed = _prehash(password)  # First truncate then pre-hash
    return pwd_context.verify(prehashed, hashed)  # Verify using bcrypt

def create_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["user_id"]
    except:
        raise HTTPException(401, "Invalid token")
