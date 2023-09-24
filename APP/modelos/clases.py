from flask import request
from APP.producto.prducto import productos
class crud:
    @staticmethod
    def post():
        producto_data = request.json
        productos.append(producto_data)
        return productos
