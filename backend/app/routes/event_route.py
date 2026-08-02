from fastapi import APIRouter, Depends, status

from app.dependencies.auth import get_current_user
from app.schemas.event_schema import EventCreate
from app.core.rabbitmq import publish_event

router = APIRouter()


@router.post(
    "/events",
    status_code=status.HTTP_202_ACCEPTED,
)
def create_event(
    event: EventCreate,
    current_user=Depends(get_current_user),
):
    publish_event(
        {
            "user_id": current_user.id,
            "event_type": event.event_type,
            "product_id": event.product_id,
            "event_data": event.event_data,
        }
    )

    return {
        "message": "Event queued successfully"
    }