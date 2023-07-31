FROM python:3.9

WORKDIR /user-superset

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV USER_URL=localhost
ENV DB_NAME=ofertas_db
ENV DB_HOST=db_ofertas
ENV DB_PORT=5432
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
COPY . .

CMD ["uvicorn", "app.main:app", " --host", "0.0.0.0:5000"]
