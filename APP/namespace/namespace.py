from flask import Blueprint
from flask_restx import Api


apiblueprint = Blueprint('api', __name__)

api = Api(apiblueprint)


