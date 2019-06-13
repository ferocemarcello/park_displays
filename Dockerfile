FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /park_displays_app

WORKDIR /park_displays_app

COPY * /park_displays_app/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]