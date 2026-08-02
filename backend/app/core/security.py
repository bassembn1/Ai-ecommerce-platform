from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings


if not settings.SECRET_KEY:
    raise RuntimeError(
        "SECRET_KEY environment variable is not set"
    )


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


""" def hash_password(password: str) -> str:
    return pwd_context.hash(password) """

def hash_password(password: str) -> str:
    print("=" * 40)
    print("Password:", repr(password))
    print("Length:", len(password))
    print("=" * 40)

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(data: dict) -> str:

    to_encode = data.copy()

    expire = (
        datetime.now(timezone.utc)
        + timedelta(days=settings.ACCESS_TOKEN_EXPIRE_DAYS)
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def verify_token(token: str) -> dict | None:

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        if "user_id" not in payload:
            return None

        return payload

    except JWTError:
        return None