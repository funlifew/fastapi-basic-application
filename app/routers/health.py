from fastapi import APIRouter
from datetime import datetime, timezone
import platform, sys

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("")
def health_check():
    return {
        'status': 'ok',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'python_version': sys.version,
        'platform': platform.system(),
    }