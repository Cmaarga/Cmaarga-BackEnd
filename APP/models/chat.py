from APP.database import DatabaseConnection

class Chat:
    @staticmethod
    def find_user(username):
        query = "SELECT * FROM usuarios WHERE usuariosusername = %s"
        #query0= "SELECT * FROM usuarios WHERE user ="
        #query1=query0+"'"+username+"'"
        result = DatabaseConnection.fetch_one(query, (username,))
        #result = DatabaseConnection.fetch_one(query1)
        if result is None:
            return None

        user = {
            'usuariosid': result[0],
            'usuariosusername': result[5],
            'usuariosnombre': result[1],
            'usuariosapellido': result[2],
            'usuariosemail': result[3],
            'usuariospassword': result[6],
            'usuariostelefono': result[4]
        }

        return user
    
    @staticmethod
    def get_user_servers(user_id):
        query = "SELECT * FROM usuarios_servidores WHERE usuario = %s"
        query1="""select se.servidoresnombre, servidoresdescripcion from servidores as se inner join usuarios_servidores as us on se.servidoresid = us.usuarios_servidoresservidor
where us.usuarios_servidoresusuario = %s"""
        results = DatabaseConnection.fetch_all(query1, (user_id,))

        servers = []
        for result in results:
            server = {
                'id': result[0],
                'servidor': result[1],
                'descripcion': result[2],
                
            }
            servers.append(server)

        return servers
    

    @staticmethod
    def create_user(username, password, nombre, apellido, email, telefono):
        try:
            # Verificar si el usuario ya existe en la base de datos
            #existing_user = Chat.find_user(username)
            #if existing_user is not None:
             #   return {'success': False, 'message': 'El usuario ya existe'}
            
            query = """INSERT INTO usuarios (usuariosnombre, usuariosapellido, usuariosemail, usuariospassword, usuariostelefono, usuariosusername) VALUES (%s, %s, %s, %s, %s, %s)"""
            values = (nombre, apellido, email, password, telefono, username)
            user_id = DatabaseConnection.execute_query(query, values)
            
            return {'success': True, 'message': 'Usuario creado exitosamente', 'user_id': user_id}
        
        except Exception as e:
            return {'success': False, 'message': 'Error al crear el usuario: {}'.format(str(e))}