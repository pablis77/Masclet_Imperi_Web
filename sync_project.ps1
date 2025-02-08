# Obtener las últimas actualizaciones del repositorio
git pull origin master

# Obtener los últimos datos desde S3 (solo si existen cambios remotos en los metadatos de DVC)
if (dvc status -q | Select-String -Pattern "modified") {
    dvc pull
}

# Añadir cambios al seguimiento de DVC (si hay cambios en matriz_master.csv)
if (git status --porcelain | Select-String -Pattern "matriz_master.csv") {
    dvc add matriz_master.csv
}

# Versionar los cambios con Git (pregunta por el mensaje de commit)
$commitMessage = Read-Host "Introduce el mensaje del commit"
if (-not $commitMessage) {
    Write-Host "No se ha introducido un mensaje de commit. Cancelando."
    exit
}
git add .
git commit -m "$commitMessage"

# Subir los datos a S3
python dvc_push_script.py

# Subir los cambios a GitHub
git push origin master

Write-Host "Proyecto sincronizado correctamente."