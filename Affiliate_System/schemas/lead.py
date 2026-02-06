from pydantic import BaseModel

class LeadCreateRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    phoneNumber: str

class LeadCreateResponse(BaseModel):
    Code: str
    LeadId: str
    Message: str
    Request_id: str
