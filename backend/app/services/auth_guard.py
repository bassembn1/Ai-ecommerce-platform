""" from fastapi import (
    Header,
    HTTPException,
)

from sqlalchemy.orm import (
    Session
)

from app.models.user import (
    User
)

from app.core.security import (
    verify_token
)


def get_current_admin(
    authorization: str,
    db: Session
):
    if not authorization:
        raise HTTPException(
            status_code=401
        )

    token = authorization.replace("Bearer ", "")

    payload = verify_token(token)

    if not payload:
        raise HTTPException(
            status_code=401
        )

    user = db.query(User).filter(User.id == payload["user_id"]).first()

    if user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail=
            "Admin only"
        )

    return user """

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.schemas.current_user import CurrentUser


def get_current_admin(
    current_user: CurrentUser = Depends(get_current_user),
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin only",
        )

    return current_user