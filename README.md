# Student Placement Prediction Web App

Predicts whether a student is likely to be placed based on academic profile, skills, and experience.

This project combines:
- A trained ML pipeline (`XGBoost` + preprocessing with `scikit-learn`)
- A FastAPI web app with a responsive HTML interface
- A retraining script for regenerating the model locally

## Why this project

Placement outcomes depend on multiple factors like CGPA, internships, aptitude, communication, projects, and backlogs.  
This app provides a quick prediction with confidence score to support analysis and learning.

## Features

- Fast placement prediction from form input
- Confidence percentage output
- Responsive UI for desktop/mobile
- POST-Redirect-GET flow to avoid duplicate form submission issues
- Session-backed result/form retention
- Reset endpoint to clear current session data
- Optional browser auto-open on app start

## Tech Stack

- Backend: FastAPI, Uvicorn
- ML/Data: pandas, scikit-learn, xgboost, joblib
- Templating/UI: Jinja2, HTML, CSS
- Form handling: python-multipart
- Session signing: itsdangerous (used by Starlette SessionMiddleware)

## Project Structure

```text
placement_web_app/
|-- main.py
|-- retrain.py
|-- requirements.txt
|-- student_placement_dataset_updated.csv
|-- model/
|   `-- placement_model.pkl
`-- templates/
    `-- index.html
```

## Input Features Used by Model

- `gender` (categorical)
- `cgpa` (0-10)
- `internships` (int)
- `aptitude_score` (0-100)
- `communication_score` (0-100)
- `projects` (int)
- `branch` (categorical)
- `backlogs` (int)

Target:
- `status` (placed / not placed)

## Setup (Local)

### 1. Clone

```bash
git clone https://github.com/AjitMahapatro/Student-Placement-Prediction-Using-ML.git
cd Student-Placement-Prediction-Using-ML
```

### 2. Create and activate virtual environment

Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train model (if needed)

```bash
python retrain.py
```

### 5. Run app

```bash
python main.py
```

Default URL:
- `http://127.0.0.1:10000`

## Environment Variables

- `PORT`  
  Default: `10000`  
  Used by `main.py` while starting Uvicorn.

- `AUTO_OPEN_BROWSER`  
  Default: `1`  
  Set `0` to disable auto opening browser on startup.

- `SESSION_SECRET_KEY`  
  Recommended in production to sign session data securely.

## API Routes

- `GET /`  
  Renders form + (if available) latest prediction from session.

- `POST /predict_form`  
  Accepts form data, predicts placement, stores output in session, redirects to `/`.

- `GET /reset`  
  Clears session form and prediction data, redirects to `/`.

## Model Training Details (`retrain.py`)

Pipeline:
1. Read dataset
2. Split features/target
3. Preprocess:
   - `StandardScaler` for numeric features
   - `OneHotEncoder(handle_unknown="ignore")` for categorical features
4. Train `XGBClassifier`:
   - `n_estimators=200`
   - `max_depth=4`
   - `learning_rate=0.05`
   - `eval_metric="logloss"`
5. Save model to `model/placement_model.pkl`

## Notebook + Script Workflow

The full data science analysis was done in Jupyter Notebook.  
A separate `retrain.py` script is included for stable training in VS Code/Python environment when notebook/runtime compatibility issues occur.

This keeps:
- Notebook for EDA/experiments
- Python script for reproducible training and deployment

## Common Troubleshooting

- `ModuleNotFoundError: No module named 'itsdangerous'`  
  Run:
  ```bash
  pip install -r requirements.txt
  ```

- Model file not found  
  Ensure `model/placement_model.pkl` exists. If not, run:
  ```bash
  python retrain.py
  ```

## Notes

- This project is for educational use and prototype-level decision support.
- Real placement outcomes also depend on factors beyond this dataset/model.

## License

MIT 
