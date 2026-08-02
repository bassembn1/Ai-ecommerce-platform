from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

from sqlalchemy.orm import Session

from app.database.db import (
    SessionLocal,
)

from app.models.user import User

from app.core.security import (
    verify_token,
)

router = APIRouter()

security = HTTPBearer()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/me")
def get_current_user(
    credentials:
    HTTPAuthorizationCredentials =
    Depends(security),

    db: Session =
    Depends(get_db),
):
    token = (
        credentials.credentials
    )

    payload = (
        verify_token(token)
    )

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    user_id = payload.get(
        "user_id"
    )

    user = (
        db.query(User)
        .filter(
            User.id == user_id
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
    }