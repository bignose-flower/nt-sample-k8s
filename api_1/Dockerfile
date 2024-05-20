FROM python:latest
WORKDIR /app
COPY requirements.txt /app/
COPY sample_api1.py /app/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "sample_api1:app", "--host", "0.0.0.0", "--port", "8001"]