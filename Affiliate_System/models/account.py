from sqlalchemy import Column, String, DateTime, ForeignKey
from database import Base
from datetime import datetime
import uuid

class Account(Base):
    __tablename__ = "accounts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    affiliate_id = Column(String, ForeignKey("affiliates.id"))
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    currency = Column(String)
    trading_platform = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
