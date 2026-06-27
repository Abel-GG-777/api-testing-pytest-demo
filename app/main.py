from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, constr


app = FastAPI(title="API Testing Demo with FastAPI")

NonEmptyString = constr(strip_whitespace=True, min_length=1)


class UserCreate(BaseModel):
    name: NonEmptyString
    email: NonEmptyString


class User(UserCreate):
    id: int


users: list[User] = [
    User(id=1, name="Alice Johnson", email="alice@example.com"),
    User(id=2, name="Bob Smith", email="bob@example.com"),
]


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a welcome message for the demo API."""
    return {"message": "API Testing Demo with FastAPI"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "ok"}


@app.get("/users", response_model=list[User])
def get_users() -> list[User]:
    """Return all demo users stored in memory."""
    return users


@app.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id: int) -> User:
    """Return one user by id or a clear 404 error."""
    for user in users:
        if user.id == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} was not found.",
    )


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> User:
    """Create a new user in memory and return the created resource."""
    next_id = max(user.id for user in users) + 1 if users else 1
    created_user = User(id=next_id, name=payload.name, email=payload.email)
    users.append(created_user)
    return created_user
