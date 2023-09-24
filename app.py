from flask import Flask
from APP.namespace.namespace import apiblueprint
from APP.rutas.endpoint import Endpoints

app = Flask(__name__)

        
app.register_blueprint(apiblueprint)

if __name__ == '__main__':
    app.run(debug=True) 
 
