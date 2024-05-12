from datetime import timedelta
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import crud
import schemas
from database import engine, get_db
from models import Base, User
from settings import ACCESS_TOKEN_EXPIRE_MINUTES

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')


@app.post("/user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
) -> schemas.Token:
    user = crud.authenticate_user(
        db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")


@app.get("/user", response_model=schemas.User)
async def read_user(
    current_user: Annotated[User, Depends(crud.get_current_user)],
):
    return current_user


@app.get("/tg_link")
async def create_tg_link(
    current_user: Annotated[User, Depends(crud.get_current_user)],
    db: Session = Depends(get_db)
):
    return {
        'tg_url':
        f'https://t.me/SymLenght_AvedsTestBot?start={current_user.tg_token}'
    }
