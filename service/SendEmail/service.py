from fastapi import APIRouter, Request, File, UploadFile, status
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from pprint import pprint
from typing import List

router = APIRouter()


@router.post("/send_email")
async def send_email(
    request: Request,
    html_template: UploadFile = File(...),
    excel_file: UploadFile = File(...),
):
    request_data = await request.form()
    request_data = jsonable_encoder(request_data)
    print("-" * 50)
    pprint(request_data)
    print("-" * 50)

    # -------------------- 儲存上傳的檔案 --------------------
    if html_template.filename and excel_file.filename:
        with open(f"service/SendEmail/{html_template.filename}", "wb") as f:
            f.write(html_template.file.read())
        with open(f"service/SendEmail/{excel_file.filename}", "wb") as f:
            f.write(excel_file.file.read())
    # -------------------------------------------------------

    return {"status": "success"}
