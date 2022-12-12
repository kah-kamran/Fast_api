from fastapi import APIRouter, Depends, HTTPException
import schemas, crud
from dependencies import get_token_header
from fastapi.security import OAuth2PasswordBearer
from typing import List
from sqlalchemy.orm import Session
from database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate , token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[schemas.Item])
def read_items(token: str = Depends(oauth2_scheme),skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items