# Utilisez une image Python 3.10 slim comme base
FROM python:3.10-slim

# Définissez le répertoire de travail
WORKDIR /app

# Copiez le code de votre API et le fichier de requirements
COPY api.py .
COPY requirements.txt .

# Mettez à jour pip et installez les dépendances
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Définissez la commande pour exécuter l'API
CMD uvicorn api:app --host 0.0.0.0 --port 8080
