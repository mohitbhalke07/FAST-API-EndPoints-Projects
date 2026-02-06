from pydantic import BaseModel

class AffiliateCreateRequest(BaseModel):
    first_name: str
    last_name: str
    password: str
    mobile: str
    country: str

class AffiliateCreateResponse(BaseModel):
    Code: str
    affiliate_id: str
    username: str
    Request_id: str

class AffiliateLoginRequest(BaseModel):
    username: str
    password: str

class AffiliateLoginResponse(BaseModel):
    Code: str
    Result: dict
    Request_id: str
