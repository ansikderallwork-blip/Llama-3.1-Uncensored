FROM llama3.1:latest
WORKDIR /app
COPY llama-3.1.model /app/model
CMD ["python", "run.py"]
