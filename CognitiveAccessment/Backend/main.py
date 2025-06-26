from fastapi import FastAPI
from endpoint import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Assessment API")

# ADD THIS ROOT ROUTE
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Assessment API. All endpoints are under /api."}


app.include_router(router, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
