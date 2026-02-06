from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import uuid

from dependencies import get_db
from core.auth import verify_affiliate_token
from models.account import Account
from schemas.account import *

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post("/add", response_model=AccountCreateResponse)
def create_account(
    payload: AccountCreateRequest,
    affiliate_id: str = Depends(verify_affiliate_token),
    db: Session = Depends(get_db)
):
    acc = Account(
        affiliate_id=affiliate_id,
        first_name=payload.firstName,
        last_name=payload.lastName,
        email=payload.email,
        phone=payload.phoneNumber,
        currency=payload.currency,
        trading_platform=payload.trading_platform
    )

    db.add(acc)
    db.commit()
    db.refresh(acc)

    return {
        "Code": "Success",
        "AccountId": acc.id,
        "TradingPlatformAccountName": "9444660",
        "TradingPlatformAccountPassword": "pass1234",
        "Request_id": f"REQ-{uuid.uuid4()}"
    }
