import os
from dotenv import load_dotenv
from flask import Flask
from app.config import Config

load_dotenv()
app = Flask(__name__)
    
def create_app(config_class = Config):
	app.config.from_object(config_class)
	
	from app.main.routes import main
		
	app.register_blueprint(main)

	return app
