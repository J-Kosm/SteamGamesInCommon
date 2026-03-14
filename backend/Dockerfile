FROM python:3.14

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run Daphne on port 8000
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "myproject.asgi:application"]