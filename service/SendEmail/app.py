from fastapi import APIRouter, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from pprint import pprint

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/email_records")
async def email_records(request: Request):
    email_records = [
        {
            "schedule_time": "2021-05-01 10:00:00",
            "email_subject": "Test email 1",
            "recipient": "example1@exmaple.com.tw",
        }
    ]
    return templates.TemplateResponse(
        "email_records.html", {"request": request, "email_records": email_records}
    )
