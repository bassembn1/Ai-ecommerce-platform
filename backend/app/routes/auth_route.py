from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.database.db import (
    SessionLocal,
)

from app.models.user import User

from app.schemas.user_schema import (
    UserCreate,
    UserLogin,
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = (
        db.query(User)
        .filter(
            User.email == user.email
        )
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    new_user = User(
    name=user.name,
    email=user.email,
    hashed_password=hash_password(user.password),
    role="customer",
)

    db.add(new_user)
    db.commit()

    return {
        "message":
        "User created successfully"
    }


""" @router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    print(">>> LOGIN ENDPOINT CALLED <<<")
    db_user = (
        db.query(User)
        .filter(
            User.email == user.email
        )
        .first()
    )


    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials",
        )

    valid_password = (
        verify_password(
            user.password,
            db_user.hashed_password,
        )
    )
    



    if not valid_password:
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials",
        )

    token = create_access_token(
    {
        "user_id": db_user.id,
        "email": db_user.email,
        "role": db_user.role,
    }
)

    return {
        "token": token
    }

 """
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    print(">>> LOGIN ENDPOINT CALLED <<<")

    db_user = (
        db.query(User)
        .filter(
            User.email == user.email
        )
        .first()
    )

    print("=" * 50)
    print("Email received:", user.email)
    print("User found:", db_user is not None)

    if not db_user:
        print("USER NOT FOUND")
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials",
        )

    print("User id:", db_user.id)
    print("Stored hash:", db_user.hashed_password)
    print("Password received:", repr(user.password))

    valid_password = verify_password(
        user.password,
        db_user.hashed_password,
    )

    print("Password valid:", valid_password)
    print("=" * 50)

    if not valid_password:
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials",
        )

    token = create_access_token(
        {
            "user_id": db_user.id,
            "email": db_user.email,
            "role": db_user.role,
        }
    )

    return {
        "token": token
    }