#!/bin/bash
# #!/bin/sh

# echo "Esperando a la base de datos..."

# while ! pg_isready -h db -U user; do
#   sleep 1
# done

# echo "Base de datos lista. Ejecutando migraciones..."

# alembic upgrade head

# echo "Iniciando FastAPI..."

# Iniciar FastAPI
/opt/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8008 --reload


