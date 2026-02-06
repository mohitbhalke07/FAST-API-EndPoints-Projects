from pydantic import BaseModel

class AccountCreateRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    phoneNumber: str
    currency: str
    trading_platform: str

class AccountCreateResponse(BaseModel):
    Code: str
    AccountId: str
    TradingPlatformAccountName: str
    TradingPlatformAccountPassword: str
    Request_id: str
