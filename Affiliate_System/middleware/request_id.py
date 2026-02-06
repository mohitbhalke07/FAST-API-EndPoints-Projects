import uuid
from fastapi import Request

async def request_id_middleware(request: Request, call_next):
    request_id = f"REQ-{uuid.uuid4()}"
    response = await call_next(request)   # Request goes to API/endpoint
    response.headers["X-Request-ID"] = request_id
    return response

# Client → Request comes in
#         → Middleware creates ID
#         → Request goes to API
#         → API returns response
#         → Middleware adds header
# Client ← Response goes back
# async allows pausing; await is where the pause happens.