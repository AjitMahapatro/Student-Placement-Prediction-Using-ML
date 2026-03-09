import os
import threading
import webbrowser

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    url = f"http://127.0.0.1:{port}"
    # Open the app automatically in the default browser on local runs.
    if os.environ.get("AUTO_OPEN_BROWSER", "1") == "1":
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    uvicorn.run("main:app", host="0.0.0.0", port=port)

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key=os.environ.get("SESSION_SECRET_KEY", "change-this-in-production")
)

templates = Jinja2Templates(directory="templates")

model = joblib.load("model/placement_model.pkl")


class StudentData(BaseModel):
    gender: str
    cgpa: float
    internships: int
    aptitude_score: int
    communication_score: int
    projects: int
    branch: str
    backlogs: int


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    form_data = request.session.get("form_data", {
        "gender": "",
        "cgpa": "",
        "internships": "",
        "aptitude_score": "",
        "communication_score": "",
        "projects": "",
        "branch": "",
        "backlogs": ""
    })
    prediction = request.session.get("prediction")
    probability_percent = request.session.get("probability_percent")

    context = {
        "request": request,
        "form_data": form_data
    }

    if prediction is not None and probability_percent is not None:
        context["prediction"] = int(prediction)
        context["probability_percent"] = float(probability_percent)

    response = templates.TemplateResponse(
        "index.html",
        context
    )
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.post("/predict_form")
async def predict_form(request: Request):

    form = await request.form()
    form_data = {
        "gender": str(form["gender"]),
        "cgpa": str(form["cgpa"]),
        "internships": str(form["internships"]),
        "aptitude_score": str(form["aptitude_score"]),
        "communication_score": str(form["communication_score"]),
        "projects": str(form["projects"]),
        "branch": str(form["branch"]),
        "backlogs": str(form["backlogs"])
    }
    
    input_data = pd.DataFrame([{
        "gender": form_data["gender"],
        "cgpa": float(form_data["cgpa"]),
        "internships": int(form_data["internships"]),
        "aptitude_score": int(form_data["aptitude_score"]),
        "communication_score": int(form_data["communication_score"]),
        "projects": int(form_data["projects"]),
        "branch": form_data["branch"],
        "backlogs": int(form_data["backlogs"])
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    probability_percent = round(float(probability) * 100, 2)

    request.session["form_data"] = form_data
    request.session["prediction"] = int(prediction)
    request.session["probability_percent"] = probability_percent
    return RedirectResponse(url="/", status_code=303)


@app.get("/reset")
def reset_form(request: Request):
    request.session.pop("form_data", None)
    request.session.pop("prediction", None)
    request.session.pop("probability_percent", None)
    return RedirectResponse(url="/", status_code=303)
