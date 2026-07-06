FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000 
EXPOSE 8501  


#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


 CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]
