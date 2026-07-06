# Insurance Status Prediction App

This project contains a FastAPI service for insurance prediction and a Streamlit UI for the same model.

## 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 2. Install dependencies

```powershell
pip install -r requirements.txt
```

## 3. Run the FastAPI app

```powershell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Open:
- http://127.0.0.1:8000/ for the home page
- http://127.0.0.1:8000/docs for Swagger UI
- http://127.0.0.1:8000/health for health check

## 4. Run the Streamlit app

```powershell
streamlit run streamlit_app.py --server.address 0.0.0.0 --server.port 8501
```

## 5. Docker build and run

Build the image:

```powershell
docker build -t insurance-status .
```

Run the FastAPI container:

```powershell
docker run --rm -p 8000:8000 insurance-status
```

Run the Streamlit container:

```powershell
docker run --rm -p 8501:8501 insurance-status streamlit run streamlit_app.py --server.address=0.0.0.0 --server.port=8501
```

## 6. Common issues and fixes

- If Python cannot find FastAPI, Streamlit, or pandas, reinstall the dependencies with `pip install -r requirements.txt`.
- If the container build fails, make sure the requirements file is saved as UTF-8 and contains the packages listed below.
- If the model file is missing, verify that the file exists at [model/model.pkl](model/model.pkl).
- If the API cannot start, confirm that the current working directory is the project root or that the model path resolves correctly.
