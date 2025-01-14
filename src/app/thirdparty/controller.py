from typing import List, Union
from fastapi import APIRouter,Depends, Query
from .dependencies import get_service
from .models import CheckClientDataRequest
from .services import ThirdpartyServices

router = APIRouter(
    prefix="/thirdparty/check",
    tags=[""]
)

@router.post("/client/",response_model=Union[dict,List])
def verify_client_data(data:CheckClientDataRequest,
                       service:ThirdpartyServices=Depends(get_service)):
    print(data)

    return service.valida_datos_cliente(data)
