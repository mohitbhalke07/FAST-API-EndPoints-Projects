from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random, uuid

from database import Base, engine
from dependencies import get_db
from models.affiliate import Affiliate
from models.token import AffiliateToken
from core.security import hash_password, verify_password, generate_token
from schemas.affiliate import *

router = APIRouter(prefix="/affiliate", tags=["Affiliate"])
Base.metadata.create_all(bind=engine)

def gen_username(country: str):
    return f"AFF{country[:2].upper()}{random.randint(100000,999999)}"

@router.post("/create", response_model=AffiliateCreateResponse)
def create_affiliate(
    payload: AffiliateCreateRequest,
    db: Session = Depends(get_db)
):
    username = gen_username(payload.country)

    affiliate = Affiliate(
        first_name=payload.first_name,
        last_name=payload.last_name,
        username=username,
        password_hash=hash_password(payload.password),
        mobile=payload.mobile,
        country=payload.country
    )

    db.add(affiliate)
    db.commit()
    db.refresh(affiliate)

    return {
        "Code": "Success",
        "affiliate_id": affiliate.id,
        "username": username,
        "Request_id": f"REQ-{uuid.uuid4()}"
    }
