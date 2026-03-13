# Student Placement Prediction Web App

An end-to-end machine learning web application that predicts whether a student is likely to be placed based on academic performance, internships, aptitude, communication skills, projects, branch, and backlogs.

This project combines a trained ML pipeline, a FastAPI backend, and a responsive web interface to provide placement predictions with a confidence score.

## Team

- Team Leader: Ajit Mahapatro
- Team Members: G. Jyothi Charan, M. Naveen, K. Kushwanth, A. Shanmukh, P. Leela, K. Harsha

## Project Overview

Placement outcomes are influenced by multiple academic and skill-based factors. This project was built to analyze those factors and generate a quick prediction that can support learning, self-assessment, and project demonstration.

The application accepts student details through a web form, processes the input using a trained machine learning model, and returns:

- Placement prediction
- Confidence percentage
- Clean, session-based result display

## Features

- Predicts student placement likelihood from structured input data
- Displays prediction confidence in percentage form
- Uses a responsive web interface for desktop and mobile
- Supports POST-Redirect-GET flow to avoid duplicate form submission
- Retains recent form data and result using session storage
- Includes a reset route to clear the current prediction
- Supports local model retraining through a separate Python script

## Tech Stack

- Backend: FastAPI, Uvicorn
- Machine Learning: scikit-learn, XGBoost
- Data Handling: pandas, joblib
- Frontend: HTML, CSS, Jinja2
- Session Handling: Starlette SessionMiddleware
- Form Support: python-multipart

## Project Structure

```text
placement_web_app/
|-- main.py
|-- retrain.py
|-- requirements.txt
|-- runtime.txt
|-- student_placement_dataset_updated.csv
|-- model/
|   `-- placement_model.pkl
`-- templates/
    `-- index.html
```

## Input Features

The model uses the following inputs:

- `gender`
- `cgpa`
- `internships`
- `aptitude_score`
- `communication_score`
- `projects`
- `branch`
- `backlogs`

Target variable:

- `status`

## How It Works

1. The user enters student details in the web form.
2. FastAPI receives the form data and converts it into a DataFrame.
3. The trained model predicts placement status.
4. The model also returns a probability score.
5. The result and confidence score are shown on the UI.

## Model Training

The training workflow is implemented in `retrain.py`.

Training pipeline:

1. Load dataset from `student_placement_dataset_updated.csv`
2. Split input features and target column
3. Preprocess numerical features using `StandardScaler`
4. Encode categorical features using `OneHotEncoder`
5. Train an `XGBClassifier`
6. Save the trained pipeline as `model/placement_model.pkl`

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AjitMahapatro/Student-Placement-Prediction-Using-ML.git
cd Student-Placement-Prediction-Using-ML
```

### 2. Create a virtual environment

Windows PowerShell:

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

### 4. Retrain the model if needed

```bash
python retrain.py
```

### 5. Run the application

```bash
python main.py
```

Default local URL:

```text
http://127.0.0.1:10000
```

## Environment Variables

- `PORT`: Port used by the FastAPI app. Default is `10000`.
- `AUTO_OPEN_BROWSER`: Set to `0` to disable automatic browser opening on startup.
- `SESSION_SECRET_KEY`: Secret key used for session signing. Recommended for production use.

## Application Routes

- `GET /` - Displays the prediction form and latest result
- `POST /predict_form` - Accepts form data and generates prediction
- `GET /reset` - Clears saved session data and resets the form

## Example Use Cases

- Student self-assessment projects
- Academic mini project demonstrations
- ML deployment practice
- FastAPI and Jinja2 integration learning

## Notes

- This project is intended for educational and demonstration purposes.
- Prediction output should not be treated as a real-world placement guarantee.
- Results depend on the quality and scope of the training dataset.

## License

MIT License
