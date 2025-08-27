import time
from typing import Any
from fastapi import APIRouter
from pydantic import BaseModel
from ..model import Response
router = APIRouter()
class Information(BaseModel):
    time:str|None =None

@router.post("/visit",response_model=Response)
async def visit_count(information:Information) -> Any:
    if information.time is None:
        information.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return Response(code=200,message="success")