from decimal import Decimal
from core.base import BaseServices
from .models import CheckClientDataRequest
from safi.repository.clientes  import CLIENTESALDOSCONBITALT,CLIENTESALDOSCON


class ThirdpartyServices(BaseServices):
    def valida_datos_cliente(self,data:CheckClientDataRequest):
        # alta en la bitacora
        alta_bitacora= CLIENTESALDOSCONBITALT.alta_BitacoraCliente(ClienteID=data.client_id,Dispositivo=data.device_id,Usuario=data.user_id)
        print(alta_bitacora.routine)
        print(alta_bitacora.parameters)
        bitacora=self.db.save(alta_bitacora)
        if bitacora.error_code>0:
            pass
        if data.key=="1":
            respuesta={}
            consulta= CLIENTESALDOSCON.consulta_ValidaDisponible(ClienteID=data.client_id,ValorReferencia=data.value)
            resultado=self.db.get(consulta)
            respuesta["is_valid"]=bool(resultado.get("Resultado"))
           
        
        
        
        return respuesta