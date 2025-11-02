from http import HTTPStatus

from fastapi import APIRouter

from app.database.engine import check_availability

router = APIRouter()

@router.get(path='/status',)
def status():
    return check_availability()

