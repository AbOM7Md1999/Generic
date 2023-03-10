FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /django

COPY . .

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]