from fastapi import FastAPI, Path
import json

app = FastAPI()

def load_data():
    try:
        with open('patients.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        # No data file yet — return empty dataset
        print('Warning: patients.json not found. Returning empty data.')
        return {}
    except json.JSONDecodeError:
        # File exists but is empty or invalid JSON
        print('Warning: patients.json contains invalid JSON. Returning empty data.')
        return {}
    except Exception as e:
        # Unexpected error — don't raise from request handler
        print('Error loading patients.json:', repr(e))
        return {}

@app.get("/")
async def read_root():
    return {"message": "Patient Management System API"}

@app.get('/about')
async def read_item():
    return {"message": "A fully functional API to manage patient's data"}

@app.get('/view-patients')
async def view_patients():
    data = load_data()
    return data

@app.get('/patients/{patient_id}')
async def read_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"message": "Patient not found"}