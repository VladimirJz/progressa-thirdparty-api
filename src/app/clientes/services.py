from core.base import BaseServices
from safi.repository.clientes import CLIENTESCON

class ClienteServices(BaseServices):
    def consulta_cliente_por_id(self,cliente_id:int=0):
        consulta_cliente=CLIENTESCON.consulta_Principal(ClienteID=cliente_id)
        datos_cliente=self.db.get(consulta_cliente)
        return datos_cliente.data
    