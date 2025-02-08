import os
from decouple import config
import subprocess

try:
    bucket_name = config('BUCKET_NAME')
    aws_region = config('AWS_DEFAULT_REGION', default='eu-west-1') # region por defecto si no esta en el .env
except Exception as e:
    print(f"Error al cargar variables de entorno desde .env: {e}")
    exit()

try:
    # Verifica si el remoto 'storage' ya existe
    result = subprocess.run(["dvc", "remote", "list"], capture_output=True, text=True, check=True)
    remotes = result.stdout.splitlines()
    storage_exists = any("storage" in remote for remote in remotes)
    if not storage_exists:
        # Añade el remoto solo si no existe
        subprocess.run(["dvc", "remote", "add", "-d", "storage", f"s3://{bucket_name}"], check=True)
        print("Remoto DVC (storage) configurado correctamente.")
    else:
        print("El remoto DVC (storage) ya existía. No se ha añadido de nuevo.")

except subprocess.CalledProcessError as e:
    print(f"Error *grave* al configurar el remoto DVC: {e}")
    exit()

try:
    subprocess.run(["dvc", "push"], check=True)
    print("DVC push ejecutado correctamente.")
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar DVC push: {e}")