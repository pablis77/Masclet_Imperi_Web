from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///masclet_imperi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# Registrar blueprints
from controllers import auth, animals, users
app.register_blueprint(auth.bp)
app.register_blueprint(animals.bp)
app.register_blueprint(users.bp)

if __name__ == '__main__':
    app.run(debug=True)