from app.thirdparty.controller import router as router_thirdparty
from fastapi import APIRouter


main_router = APIRouter(
    prefix="/api/v1"
)
main_router.include_router(router_thirdparty)
