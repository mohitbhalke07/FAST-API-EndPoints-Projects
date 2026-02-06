from fastapi import FastAPI
from routers import affiliate, accounts, leads
from middleware.request_id import request_id_middleware

app = FastAPI(title="Affiliate API")

app.middleware("http")(request_id_middleware)

app.include_router(affiliate.router)
app.include_router(accounts.router)
app.include_router(leads.router)