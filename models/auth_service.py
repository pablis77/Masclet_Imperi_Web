import os
import json
import hashlib
import logging
from cryptography.fernet import Fernet
from config.settings import ROLES
import sys

class AuthService:
    def __init__(self, username_var, password_var, recordar_var, encryption_key):
        # Determinar la ruta base
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.dirname(os.path.dirname(__file__))
        
        # Configurar ruta del archivo de usuarios
        self.data_dir = os.path.join(base_path, 'data')
        os.makedirs(self.data_dir, exist_ok=True)
        self.users_file = os.path.join(self.data_dir, 'users.json')
        
        print(f"Users file path: {self.users_file}")  # Debug print
        
        self.username_var = username_var
        self.password_var = password_var
        self.recordar_var = recordar_var
        self.key = encryption_key
        self.cipher_suite = Fernet(self.key)
        
        # Cargar o crear usuarios
        if os.path.exists(self.users_file):
            self.load_users()
        else:
            self.usuarios = {
                "admin": {
                    "password": hashlib.sha256("admin123".encode()).hexdigest(),
                    "role": "administrador"
                },
                "editor": {
                    "password": hashlib.sha256("editor123".encode()).hexdigest(),
                    "role": "editor"
                },
                "user": {
                    "password": hashlib.sha256("user123".encode()).hexdigest(),
                    "role": "usuario"
                }
            }
            self.save_users()
    
    def load_users(self):
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error cargando usuarios: {e}")
        
        # Si no existe el archivo o hay error, crear usuarios por defecto
        default_users = {
            "admin": {
                "password": hashlib.sha256("admin123".encode()).hexdigest(),
                "role": "administrador"
            },
            "editor": {
                "password": hashlib.sha256("editor123".encode()).hexdigest(),
                "role": "editor"
            },
            "user": {
                "password": hashlib.sha256("user123".encode()).hexdigest(),
                "role": "usuario"
            }
        }
        self.save_users(default_users)
        return default_users

    def save_users(self, users=None):
        try:
            if users is None:
                users = self.usuarios
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(users, f, indent=4)
            print(f"Usuarios guardados en: {self.users_file}")
            return True
        except Exception as e:
            print(f"Error guardando usuarios: {e}")
            return False

    def cargar_credenciales(self):
        try:
            credentials_file = os.path.join(self.data_dir, 'credentials.dat')
            if os.path.exists(credentials_file):
                with open(credentials_file, 'rb') as file:
                    datos_encrypted = file.read()
                    datos_decrypted = self.cipher_suite.decrypt(datos_encrypted)
                    datos = json.loads(datos_decrypted.decode())
                    
                    self.username_var.set(datos['username'])
                    self.password_var.set(datos['password'])
                    self.recordar_var.set(True)
                    return True
            return False
        except Exception as e:
            logging.error(f"Error al cargar credenciales: {e}")
            return False

    def guardar_credenciales(self, username, password):
        try:
            credentials_file = os.path.join(self.data_dir, 'credentials.dat')
            if self.recordar_var.get():
                datos = {
                    'username': username,
                    'password': password
                }
                datos_encoded = json.dumps(datos).encode()
                datos_encrypted = self.cipher_suite.encrypt(datos_encoded)
                
                with open(credentials_file, 'wb') as file:
                    file.write(datos_encrypted)
            else:
                if os.path.exists(credentials_file):
                    os.remove(credentials_file)
        except Exception as e:
            logging.error(f"Error al guardar credenciales: {e}")

    def verify_credentials(self, username, password):
        """Verifica las credenciales del usuario"""
        if username not in self.usuarios:
            return False
            
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return self.usuarios[username]["password"] == password_hash
        
    def has_permission(self, user_role, action):
        """Verifica si el rol tiene permiso para la acción"""
        return action in ROLES.get(user_role, [])