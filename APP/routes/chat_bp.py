from flask import Blueprint, jsonify, request
from APP.controllers.chat_controller import ChatController

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/login', methods=['POST'])
def login():
    # Obtener los datos de la solicitud (nombre de usuario y contraseña)
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Llamar al controlador para la lógica de autenticación
    result = ChatController.login(username, password)

    # Retornar la respuesta como JSON
    return jsonify(result)

@chat_bp.route('/create_user', methods=['POST'])

def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    telefono = data.get('telefono')
    
    result = ChatController.create_user(username, password, nombre, apellido, email, telefono)
    
    return jsonify(result)

