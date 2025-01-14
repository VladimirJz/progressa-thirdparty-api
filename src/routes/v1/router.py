from app.clientes.controller import router as router_clientes
from fastapi import APIRouter


main_router = APIRouter(
    prefix="/api/v1"
)
main_router.include_router(router_clientes)
