from APP.database import DatabaseConnection

class User:
    _keys=["canalesid","canalesnombre","canalesdescripcion","canalesservidor","canalescreado_por"]
    def __init__(self,**kwargs):
        self.canales_id=kwargs.get("canalesid")
        self.canales_name= kwargs.get("canalesnombre")
        self.canales_description= kwargs.get("canalesdescripcion")
        self.canales_server= kwargs.get("canalesservidor")
        self.canales_creator= kwargs.get("canalescreado_por")

    def serialize(self):
        return {
            'canalesid': self.canales_id,
            'canalesnombre': self.canales_name,
            'canalesdescripcion': self.canales_description,
            'canalesservidor': self.canales_server,
            'canalescreado_por': self.canales_creator
        }
        
    @classmethod
    def create(cls, canal):
        query = """INSERT INTO disgord.canales (canalesnombre, canalesdescripcion, canalesservidor , canalescreado_por) VALUES (%(canales_name)s, %(canales_description)s, %(canales_server)s, %(canales_creator)s)"""
        params = canal.__dict__
        DatabaseConnection.execute_query(query, params)
    @classmethod
    def get (cls, canal=None):
        if canal is not None and canal.canales_id is not None:
            query = """SELECT canalesid , canalesnombre, canalesdescripcion, canalesservidor , canalescreado_por FROM disgord.canales WHERE  usuariosid= %(user_id)s"""
            params = canal.__dict__
            result = DatabaseConnection.fetch_one(query, params)
            if result:
                return cls(**dict(zip(cls._keys, result)))
            else:
                return None
        else:
            query = "SELECT canalesid , canalesnombre, canalesdescripcion, canalesservidor , canalescreado_por FROM disgord.canales"
            results = DatabaseConnection.fetch_all(query)
            users = []
            for row in results:
                users.append (cls(**dict(zip(cls._keys, row))))
            return users
    
