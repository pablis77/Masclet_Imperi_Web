import os
import sys

class PathManager:
    @staticmethod
    def get_base_path():
        """Obtiene la ruta base de la aplicación"""
        base_path = ''
        if getattr(sys, 'frozen', False):
            # Ejecutable
            base_path = os.path.dirname(sys.executable)
        else:
            # Desarrollo
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(f"Base path: {base_path}")  # Debug
        return base_path
    
    @staticmethod
    def ensure_directories():
        """Asegura que existan todos los directorios necesarios"""
        base_path = PathManager.get_base_path()
        
        dirs = {
            'data': os.path.join(base_path, 'data'),
            'config': os.path.join(base_path, 'config'),
            'backups': os.path.join(base_path, 'backups')
        }
        
        for dir_path in dirs.values():
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                
        return dirs
    
    @staticmethod
    
    def get_file_path(filename, directory='data'):
        """Obtiene la ruta completa de un archivo"""
        base_path = PathManager.get_base_path()
        full_path = os.path.join(base_path, directory, filename)
        print(f"Intentando acceder a: {full_path}")  # Debug
        print(f"¿Archivo existe?: {os.path.exists(full_path)}")  # Debug
        return full_path