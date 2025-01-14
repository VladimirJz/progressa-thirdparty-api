from fastapi import FastAPI
#from routes.v1.router import main_router
from routes.v1.router import main_router


app = FastAPI(
    debug=True,
    title="API Rest de Ejemplo",
    
    )

app.include_router(main_router)


