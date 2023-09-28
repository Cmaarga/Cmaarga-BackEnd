from APP.database import DatabaseConnection

class Server:
    _keys=["user_id","username","password","email","telefono"]
    def __init__(self,**kwargs):
        self.user_id=kwargs.get("user_id")
        self.username= kwargs.get("username")
        self.password= kwargs.get("password")
        self.email= kwargs.get("email")
        self.profile_image= kwargs.get("telefono")
        print(self.user_id)

    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'telefono': self.profile_image
        }
       
    @classmethod
    def create(cls, user):
        query = """INSERT INTO disgord.usuarios (usuariosnombre, usuariosapellido, usuariosemail, usuariospassword, usuariostelefono, usuariosusername) VALUES (%(username)s, %(password)s, %(email)s, %(profile_image)s)"""
        params = user.__dict__
        DatabaseConnection.execute_query(query, params)
    @classmethod
    def get (cls, user=None):
        if user is not None and user.user_id is not None:
            query = """SELECT usuariosid, usuariosusername, usuariospassword, usuariosemail, usuariostelefono FROM disgord.usuarios WHERE  usuariosid= %(user_id)s"""
            params = user.__dict__
            result = DatabaseConnection.fetch_one(query, params)
            if result:
                return cls(**dict(zip(cls._keys, result)))
            else:
                return None
        else:
            query = "SELECT usuariosid, usuariosusername, usuariospassword, usuariosemail, usuariostelefono FROM disgord.usuarios"
            results = DatabaseConnection.fetch_all(query)
            users = []
            for row in results:
                users.append (cls(**dict(zip(cls._keys, row))))
            return users
