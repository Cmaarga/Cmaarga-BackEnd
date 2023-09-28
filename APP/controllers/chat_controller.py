from APP.models.chat import Chat

class ChatController:
    @staticmethod
    def login(username, password):
        try:
            # Llamar al modelo para buscar el usuario en la base de datos
            user = Chat.find_user(username)
            print(user)
            
            if user is None:
                return {'success': False, 'message': 'Usuario no encontrado'}
            
            contrasenia = user.get('usuariospassword')  # Utilizamos el método get() para obtener la contraseña
            
            if contrasenia is None:  # Verificamos si la contraseña no está definida en el diccionario
                return {'success': False, 'message': 'Contraseña no definida'}
            
            print(contrasenia)
            
            if contrasenia != password:
                return {'success': False, 'message': 'Contraseña incorrecta'}
            else:
                
                servers= Chat.get_user_servers(user.get('usuariosid'))
                
                return {'success': True, 'message': 'Inicio de sesión exitoso', 'servers': servers}
        
        except Exception as e:
            return {'success': False, 'message': 'Error durante el inicio de sesión: {}'.format(str(e))}
        

    @staticmethod
    def create_user(username, password, nombre, apellido, email, telefono):
        try:
            # Verificar si el usuario ya existe en la base de datos
            existing_user = Chat.find_user(username)
            if existing_user is not None:
                return {'success': False, 'message': 'El usuario ya existe'}
            
            # Crear un nuevo usuario en la base de datos
            user_id = Chat.create_user(username, password, nombre, apellido, email, telefono)
            
            return {'success': True, 'message': 'Usuario creado exitosamente', 'user_id': user_id}
        
        except Exception as e:
            return {'success': False, 'message': 'Error al crear el usuario: {}'.format(str(e))}