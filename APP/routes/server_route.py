from flask import Blueprint
from ..controllers.server_controller import ServerController

bp_servers= Blueprint("servers",__name__)
bp_servers.route("/", methods=["GET"])(ServerController.get)
bp_servers.route("/", methods=["POST"])(ServerController.create)