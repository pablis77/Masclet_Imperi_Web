# utils/logger.py
import logging
import os

def setup_logging():
    # Crear directorio de logs si no existe
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configurar el logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/app.log'),
            logging.StreamHandler()
        ]
    )

    return logging