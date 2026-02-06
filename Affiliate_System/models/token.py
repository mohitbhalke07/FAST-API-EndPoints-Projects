from sqlalchemy import Column, String, DateTime, ForeignKey
from database import Base
from datetime import datetime
import uuid

class AffiliateToken(Base):
    __tablename__ = "affiliate_tokens"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    affiliate_id = Column(String, ForeignKey("affiliates.id"), nullable=False)
    token = Column(String, unique=True, index=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
