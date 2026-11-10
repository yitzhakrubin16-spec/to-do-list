from flask import Flask
from flask_cors import CORS  
from app.routes.tasks_routes import tasks_bp

def create_app():
    app = Flask(__name__)
    
    CORS(app, resources={
        r"^/tasks(?:/.*)?$": {
            "origins": [
                "http://localhost:5173",
                "http://127.0.0.1:5173"
            ]
        }
    }) 
    
    app.register_blueprint(tasks_bp)

    return app