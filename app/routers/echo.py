from fastapi import APIRouter
from app.schemas import MessageRequest

router = APIRouter(prefix="/echo", tags=['Echo'])


@router.post("")
def echo_message(data: MessageRequest):
    return {
        'status': 'success',
        'received_message': data.message,
    }