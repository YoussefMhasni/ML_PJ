FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

#(pour lancer le workspace dans l'image Docker)
CMD python project.py && evidently --workspace ./app/workspace --host 0.0.0.0 --port 8082



#CMD python project.py && evidently ui --host 0.0.0.0 --port 8082
