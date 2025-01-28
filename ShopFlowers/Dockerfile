FROM python:3.11.9-slim AS dependencies

WORKDIR /dependencies

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11.9-slim

WORKDIR /app

COPY --from=dependencies /dependencies/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]