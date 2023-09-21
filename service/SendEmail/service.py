from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from pprint import pprint

router = APIRouter()


@router.post("/send_email")
async def send_email(request: Request):
    data_body = await request.form()
    data_json_body = jsonable_encoder(data_body)
    pprint(data_json_body)
    return RedirectResponse(url="/home", status_code=status.HTTP_302_FOUND)
