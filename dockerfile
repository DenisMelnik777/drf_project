FROM python:3

WORKDIR /app/edu

COPY ./req_test.txt .

RUN pip install --no-cache-dir -r req_test.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]