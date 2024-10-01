from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.config.settings import Settings
from src.routers import category, product, group
from fastapi.middleware.cors import CORSMiddleware

settings = Settings()

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(category.router)
app.include_router(product.router)
app.include_router(group.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return RedirectResponse(url="/docs")
