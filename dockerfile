FROM python:3

WORKDIR /usr/src/myapp

RUN python -m venv mi_env


COPY . .

RUN mi_env/bin/pip install -r requirements.txt

EXPOSE 8000

CMD [ "mi_env/bin/python", "manage.py", "runserver", "0.0.0.0:8000" ]
