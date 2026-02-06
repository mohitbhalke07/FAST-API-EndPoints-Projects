from pydantic import BaseModel

class BaseResponse(BaseModel):
    Code: str
    Request_id: str
