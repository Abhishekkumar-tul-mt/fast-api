# Fast API — Patient Management & Prediction

This repository contains a small FastAPI backend and a Streamlit frontend for a patient-management / risk-prediction demo.

Files of interest
- `app.py` — FastAPI app that loads a pickled model and exposes `/predict`.
- `main.py` — simple FastAPI example with a few patient endpoints (`/`, `/view-patients`, `/patients/{id}`).
- `frontend.py` — Streamlit frontend that posts to the prediction API.
- `patients.json` — sample patient data used by `main.py`.
- `model.pkl` — pickled scikit-learn model used by `app.py`.

Quick setup (macOS / zsh)

1. Open a terminal in the project root:

```bash
cd /Users/abhishekkumar/Documents/fast-api
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv myenv
source myenv/bin/activate
# On fish/cmd/powershell use the correct activate script in myenv/bin/
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Notes on scikit-learn compatibility
- The pickled model in `model.pkl` was created with scikit-learn 1.6.1. To avoid unpickle errors, `requirements.txt` pins scikit-learn to `1.6.1`.

Run the API (model-backed)

Start the FastAPI app that serves the model (this file loads `model.pkl`):

```bash
# Use the venv python so the uvicorn installed in the venv is used
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

Endpoints to test (example):

```bash
curl http://127.0.0.1:8000/docs   # interactive API docs
curl -X POST http://127.0.0.1:8000/predict -H 'Content-Type: application/json' -d '{"age":30,"weight":70,"height":1.7,"income_lpa":10.0,"smoker":false,"city":"Mumbai","occupation":"Salaried"}'
```

Run the example patient API

```bash
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
curl http://127.0.0.1:8000/view-patients
curl http://127.0.0.1:8000/patients/P001
```

Run the Streamlit frontend

```bash
streamlit run frontend.py
# then open http://localhost:8501 in your browser
```

Troubleshooting
- If you see JSONDecodeError when calling `/view-patients`, ensure `patients.json` is present and valid JSON. The server logs will show warnings if the file is missing or invalid.
- If you get pickle/unpickle AttributeError for sklearn internals, make sure scikit-learn is installed at the pinned version (1.6.1) in the active environment.
- If Streamlit shows a blank page: open your browser DevTools → Console and look for JS errors or websocket connection problems. Try an incognito window or disable extensions.

Development and Git
- Repo was initialized locally and can be pushed to GitHub. Example commands:

```bash
# set remote (replace with your repo URL)
git remote add origin https://github.com/<youruser>/fast-api.git
git branch -M main
git push -u origin main
```

License
- This repo contains demo code. Add a license file if you plan to publish.
