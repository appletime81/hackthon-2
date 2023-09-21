from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


import service.SendEmail.service as SendEmailService
import service.SendEmail.app as SendEmailApp


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(SendEmailService.router, tags=["SendEmail"])
app.include_router(SendEmailApp.router, tags=["SendEmail"])


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    email_records = [
        {
            "schedule_time": "2021-05-01 10:00:00",
            "email_subject": "Test email 1",
            "recipient": "example1@exmaple.com.tw",
        }
    ]
    return templates.TemplateResponse(
        "index.html", {"request": request, "email_records": email_records}
    )
