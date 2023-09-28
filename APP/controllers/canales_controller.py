from flask import request, jsonify
from APP.database import DatabaseConnection
from APP.models.canales_models import Canal  # Importa el modelo Canal

class CanalesController:
    @staticmethod
    def get():
        query = "SELECT * FROM canales"
        result = DatabaseConnection.fetch_all(query)
        return jsonify(result)

    @staticmethod
    def get_by_id(canalesid):
        query = "SELECT * FROM canales WHERE canalesid = %s"
        result = DatabaseConnection.fetch_one(query, (canalesid,))
        if result:
            return jsonify(result)
        else:
            return 'Canal no encontrado', 404

    @staticmethod
    def create():
        canalesnombre = request.json['canalesnombre']
        canalesdescripcion = request.json['canalesdescripcion']
        canalesservidor = request.json['canalesservidor']
        canalescreado_por = request.json['canalescreado_por']

        # Crear una instancia del modelo Canal
        nuevo_canal = Canal(None, canalesnombre, canalesdescripcion, canalesservidor, canalescreado_por)

        # Llamada a la API para invocar el método create del controlador
        try:
            # Suponiendo que tienes un método en DatabaseConnection para crear un canal
            nuevo_canal_id = DatabaseConnection.create_canal(nuevo_canal)
            return f'Canal creado con ID: {nuevo_canal_id}', 201
        except Exception as e:
            return f'Error al crear el canal: {str(e)}', 500

    @staticmethod
    def update(canalesid):
        updated_data = request.json
        query = "UPDATE canales SET canalesnombre=%s, canalesdescripcion=%s, canalesservidor=%s, canalescreado_por=%s WHERE canalesid=%s"
        params = (updated_data['canalesnombre'], updated_data['canalesdescripcion'], updated_data['canalesservidor'], updated_data['canalescreado_por'], canalesid)
        DatabaseConnection.execute_query(query, params)

        return 'Canal actualizado', 200

    @staticmethod
    def delete(canalesid):
        query = "DELETE FROM canales WHERE canalesid = %s"
        params = (canalesid,)
        DatabaseConnection.execute_query(query, params)

        return 'Canal eliminado', 200
