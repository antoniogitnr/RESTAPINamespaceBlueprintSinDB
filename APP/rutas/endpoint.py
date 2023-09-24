from APP.namespace.namespace import api
from APP.producto.prducto import productos
from APP.db.tablas import producto
from flask_restx import Resource,fields
from flask import jsonify,request

class Productos:
    @api.route("/addproducts", methods=["POST"])
    class addProductos(Resource):
        @api.expect(producto,validate=True)
        def post(self):
            producto_data = request.json
            productos.append(producto_data)
            return jsonify({"status": "ok", "message": "Producto agregado exitosamente.", "productos": productos})



    @api.route("/products")
    class listarproductos(Resource):
        def get(self):
            return jsonify(productos) 
        
    @api.route("/oneproducto/<int:id_producto>")
    class getproducto(Resource):
        def get(self,id_producto):
            for producto in productos:
                if producto['id'] == id_producto:
                    return jsonify(producto)
            return jsonify({"status":"error","message":"Producto no encontrado"})
            
    @api.route("/deleteproducto/<int:id_producto>", methods=["DELETE"])
    class deleteproducto(Resource):
        def delete(self,id_producto):
            for producto in productos:
                if producto['id'] == id_producto:
                    productos.remove(producto)
                    return jsonify({"status": "ok", "message": "Producto eliminado exitosamente.", "productos": productos})
            return jsonify({"status": "error", "message": "Producto no encontardo.", "productos": productos})
        
    @api.route("/updateproducto/<int:id_producto>", methods=["PUT"])
    class updateproducto(Resource):
        @api.expect(api.model("Producto", {
            "id": fields.Integer(requiered=True, description="id producto"),
            "name": fields.String(required=True, description="nombre producto"),
            "price": fields.Integer(required=True, description="precio producto"),
            "quantity": fields.Integer(required=True, description="cantidad producto")
            }), validate=True)
        def put(self, id_producto):
            producto_data = request.get_json()
            for producto in productos:
                if producto["id"] == id_producto:
                    producto["id"] = producto_data["id"]
                    producto["name"] = producto_data["name"]
                    producto["price"] = producto_data["price"]
                    producto["quantity"] = producto_data["quantity"]
                    return jsonify({"status": "ok", "message": "Producto actualizado exitosamente.", "productos": productos})
            return jsonify({"status": "error", "message": "No se encontró el producto."})
            
                    