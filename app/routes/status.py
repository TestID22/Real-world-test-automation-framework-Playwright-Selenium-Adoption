from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()

@router.get(path='/status')
def get_status():
    return HTTPStatus.OK

