from dotenv import load_dotenv
import os
from flask import Flask

# Cargar variables de entorno desde .env
load_dotenv()

# Acceder a las variables
DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

# Configurar Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

if __name__ == '__main__':
    app.run(debug=True)