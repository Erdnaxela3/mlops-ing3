FROM python:3.11.10-slim

LABEL org.opencontainers.image.authors="Alexandre WENG <alexandre.weng@epita.fr>"

WORKDIR /web_api

COPY requirements.txt web_service.py regression.joblib ./
RUN pip install -r requirements.txt

RUN adduser --system --no-create-home nonroot
USER nonroot

EXPOSE 8042
CMD ["uvicorn", "web_service:app", "--host", "0.0.0.0", "--port", "8042"]