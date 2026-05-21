# 🎓 Student Placement Prediction System

A machine learning-based web application designed to predict student placement outcomes based on academic performance, internships, aptitude, communication skills, projects, and related factors.

The project combines machine learning workflows with a FastAPI-powered backend and a responsive web interface to provide placement predictions and confidence-based insights.

Developed as a collaborative team project during the Machine Learning with Python Internship at Adhoc Network Tech Company.

---

# 👥 Team

## Team Leader
- Ajit Mahapatro

## Team Members
- G. Jyothi Charan
- M. Naveen
- K. Kushwanth
- A. Shanmukh
- P. Leela
- K. Harsha

---

# 📌 Project Overview

This project was developed to explore how machine learning can be applied to academic and skill-based datasets to analyze placement trends and prediction patterns.

The application accepts structured student input data and generates:
- placement prediction
- confidence-based prediction score
- interactive result display

The project also provided practical exposure to deploying machine learning workflows using FastAPI.

---

# 🚀 Key Features

## Placement Prediction
- Predicts student placement likelihood
- Confidence-based prediction output
- Structured input-based analysis

---

## Machine Learning Workflow
- Data preprocessing and feature engineering
- Classification-based prediction pipeline
- Model training and evaluation using XGBoost

---

## Interactive Web Interface
- Responsive user interface
- Session-based result handling
- Simple and user-friendly workflow

---

## Model Retraining Support
- Separate training pipeline for retraining models
- Pipeline persistence using Joblib

---

# 🤖 Machine Learning Pipeline

The project uses:
- Scikit-Learn
- XGBoost
- Pandas

The workflow includes:
- preprocessing numerical and categorical features
- encoding and scaling
- classification model training
- prediction probability generation

---

# 🛠️ Tech Stack

## Backend
- FastAPI
- Uvicorn

## Machine Learning
- Scikit-Learn
- XGBoost
- Pandas
- Joblib

## Frontend
- HTML
- CSS
- Jinja2

---

# 📂 Project Structure

```text
placement_web_app/
│
├── main.py
├── retrain.py
├── requirements.txt
├── model/
│   └── placement_model.pkl
│
├── templates/
│   └── index.html
│
└── dataset/
```

---

# 📊 Input Features

The model uses:
- CGPA
- internships
- aptitude score
- communication score
- projects
- branch
- backlogs

Target Variable:
- placement status

---

# ⚙️ Workflow

```text
Student Input
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Machine Learning Prediction
      ↓
Confidence Score Generation
      ↓
Result Visualization
```

---

# 💻 Local Setup

## Clone Repository

```bash
git clone <repo-url>
cd Student-Placement-Prediction-Using-ML
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Retrain Model (Optional)

```bash
python retrain.py
```

---

## Run Application

```bash
python main.py
```

Application runs on:

```text
http://127.0.0.1:10000
```

---

# 🌐 Application Features

- Placement prediction form
- Confidence score visualization
- Session-based result management
- Reset prediction workflow

---

# 📈 Future Improvements

- Interactive analytics dashboard
- Placement trend visualization
- Real-world dataset integration
- Advanced predictive modeling
- Improved UI/UX design

---

# ⚠️ Notes

- This project was developed for educational and analytical purposes.
- Prediction results are dependent on dataset quality and model training conditions.
- The system is intended for learning and demonstration purposes only.

---

# 🎯 Learning Outcomes

This project helped strengthen practical skills in:
- machine learning workflows
- data preprocessing
- FastAPI integration
- classification modeling
- frontend-backend integration
- collaborative project development

---

# 👤 Author

Ajit Mahapatro  
B.Sc. Data Science – Aditya Degree College
