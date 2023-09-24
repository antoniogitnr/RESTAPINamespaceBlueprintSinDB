from flask import request,jsonify
from APP.producto.prducto import productos
class crud:
    @staticmethod
    def post():
        producto_data = request.json
        productos.append(producto_data)
        return productos

    
    @staticmethod
    def all():
        return jsonify({"status": "ok", "message": "Lista Productos", "productos": productos})

    
    @staticmethod 
    def one(id_producto):
        for producto in productos:
            if producto['id'] == id_producto:
                return jsonify({"status": "ok", "message": "Producto encontrado", "producto": producto})

        
    @staticmethod
    def dell(id_producto):
        for producto in productos:
            print(producto['id'])
            if producto['id'] == id_producto:
                productos.remove(producto)
                return jsonify({"status":"ok","message":"Producto eliminado","Productos":productos})
        return jsonify({"status":"error","message":"Producto no encontrado","Productos":productos})
                 
    @staticmethod
    def update(id_producto):
        producto_data = request.get_json()
        for producto in productos:
            if producto["id"] == id_producto:
                producto["id"] = producto_data["id"]
                producto["name"] = producto_data["name"]
                producto["price"] = producto_data["price"]
                producto["quantity"] = producto_data["quantity"]
                return jsonify({"status": "ok", "message": "Producto actualizado exitosamente.", "productos": productos})
        return jsonify({"status": "error", "message": "No se encontró el producto."})
        