from flask import Blueprint
from app.controllers.saludo import saludo

bp_saludo = Blueprint('api', __name__)
bp_saludo.route('/saludo')(saludo)

