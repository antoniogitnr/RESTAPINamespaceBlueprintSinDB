from APP.namespace.namespace import api
from APP.producto.prducto import productos
from APP.db.tablas import producto
from flask_restx import Resource,fields
from flask import jsonify,request
from APP.modelos.clases import crud

class Endpoints:
    @api.route("/addproducts", methods=["POST"])
    class addProductos(Resource):
        @api.expect(producto,validate=True)
        def post(self):
            productos = crud().post()
            return jsonify({"status": "ok", "message": "Producto agregado exitosamente.", "productos": productos})

    @api.route("/products")
    class listarproductos(Resource):
        def get(self):
            return crud().all()
        
    @api.route("/oneproducto/<int:id_producto>")
    class getproducto(Resource):
        def get(self,id_producto):
            return crud().one(id_producto)
            
    @api.route("/deleteproducto/<int:id_producto>", methods=["DELETE"])
    class deleteproducto(Resource):
        def delete(self,id_producto):
            return crud().dell(id_producto)
        
    @api.route("/updateproducto/<int:id_producto>", methods=["PUT"])
    class updateproducto(Resource):
        @api.expect(api.model("Producto", {
            "id": fields.Integer(requiered=True, description="id producto"),
            "name": fields.String(required=True, description="nombre producto"),
            "price": fields.Integer(required=True, description="precio producto"),
            "quantity": fields.Integer(required=True, description="cantidad producto")
            }), validate=True)
        def put(self, id_producto):
            return crud().update(id_producto)
                    