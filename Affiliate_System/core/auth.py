from fastapi import Header, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from dependencies import get_db
from models.token import AffiliateToken

def verify_affiliate_token(authorization: str = Header(...), db: Session = Depends(get_db)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token_value = authorization.split(" ")[1]

    token = db.query(AffiliateToken).filter(AffiliateToken.token == token_value).first()

    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")

    if token.expires_at < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Token expired")

    return token.affiliate_id
