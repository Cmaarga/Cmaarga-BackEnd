from flask import request
from ..models.server_model import Server
#este controller hay q modificar e implementar las mismas funciones que tiene el user controller (get, create, delete)
#lo mismo para user_model
class ServerController:
    @classmethod
    def get(cls):
        servers =[]
        for servers in Server.get():
            servers.append(servers.serialize())
        return servers, 200
    @classmethod
    def get_by_id(cls, server_id):
        server=Server(server_id=server_id)
        server = Server.get(server)
        print(server)
        if server:
            return server.serialize(), 200
    @classmethod
    def create(cls):
        data = request.get_json()
        Server = Server(
            servername=data.get("Servidor"),
            serverdescription=data.get("Descripción"),
        )
        Server.create(Server)
        return {"message": "Servidor creado Correctamente"}, 201
    def get_servers(cls,server_id):
        server = Server(server_id=server_id)
        servers=[]
        for server in Server.get_servers(server):
            print(server)
            servers.append(server.serialize())
        return servers,200
    