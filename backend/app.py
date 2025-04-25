from fastapi import FastAPI

from backend.routes.profiles import router as profiles_router
from backend.routes.search import router as search_router
from backend.routes.explain import router as explain_router


ROUTE_PREFIX = "/aifindr/api/v1"



app = FastAPI()


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