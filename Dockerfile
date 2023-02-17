FROM python:3.12.0a5
ENV PYTHONUNBUFFERED=1
ENV USERS_FILE="/persistencia/usuarios.json"
RUN pip3 install telebot
RUN mkdir /app
COPY *.py /app
CMD [ "/usr/local/bin/python3", "/app/mensajes.py" ]