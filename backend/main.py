import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
load_dotenv()

from routes.profiles import router as profiles_router
from routes.search import router as search_router
from routes.explain import router as explain_router


ROUTE_PREFIX = "/aifindr/api/v1"



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    profiles_router,
    prefix=ROUTE_PREFIX,
    tags=["v1"],
)

app.include_router(
    search_router,
    prefix=ROUTE_PREFIX,
    tags=["v1"],
)

app.include_router(
    explain_router,
    prefix=ROUTE_PREFIX,
    tags=["v1"],
) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)