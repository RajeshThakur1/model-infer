FROM python:3.8.2-buster
LABEL org.opencontainers.image.authors="rajeshthakur1r@gmail.com"
COPY . /opt
WORKDIR /opt
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install "uvicorn[standard]" gunicorn
CMD ["gunicorn", "main:app", "--workers", "1", "--timeout", "0", "--worker-class", "uvicorn.workers.UvicornH11Worker", "--bind", "0.0.0.0:5002"]