from flask import Flask, request, Blueprint

from pilots.controllers import *
pilots_routes : Blueprint = Blueprint('pilots_routes', __name__)

def register_routes(app: Flask):
    app.register_blueprint(pilots_routes)

@pilots_routes.route("/pilots", methods=['GET', 'POST'])
def list_create_pilots() -> str:
    if request.method == 'GET': return list_all_pilots()
    if request.method == 'POST': return create_pilot()
    else: return 'Method is Not Allowed'

@pilots_routes.route("/pilots/<pilot_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_pilots(pilot_id: str) -> str:
    if request.method == 'GET': return retrieve_pilot(pilot_id)
    if request.method == 'PUT': return update_pilot(pilot_id)
    if request.method == 'DELETE': return delete_pilot(pilot_id)
    else: return 'Method is Not Allowed'