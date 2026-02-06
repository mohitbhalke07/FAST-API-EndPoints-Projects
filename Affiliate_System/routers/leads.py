from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import uuid

from dependencies import get_db
from core.auth import verify_affiliate_token
from models.lead import Lead
from schemas.lead import *

router = APIRouter(prefix="/leads", tags=["Leads"])

@router.post("/add", response_model=LeadCreateResponse)
def create_lead(
    payload: LeadCreateRequest,
    affiliate_id: str = Depends(verify_affiliate_token),
    db: Session = Depends(get_db)
):
    lead = Lead(
        affiliate_id=affiliate_id,
        first_name=payload.firstName,
        last_name=payload.lastName,
        email=payload.email,
        phone=payload.phoneNumber
    )

    db.add(lead)
    db.commit()
    db.refresh(lead)

    return {
        "Code": "Success",
        "LeadId": lead.id,
        "Message": "Lead Created Successfully",
        "Request_id": f"REQ-{uuid.uuid4()}"
    }
