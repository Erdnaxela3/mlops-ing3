FROM python:3.11.10-slim

LABEL org.opencontainers.image.authors="Alexandre WENG <alexandre.weng@epita.fr>"

WORKDIR /web_api

COPY requirements.txt app.py ./
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8042
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8042"]