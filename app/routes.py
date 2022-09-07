from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.config import SessionLocal
from sqlalchemy.orm import Session
from app.schemas import UserSchema, Request, Response, RequestUser

import app.crud as crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup")
async def create_user_service(request: RequestUser, db: Session = Depends(get_db)):
    x = crud.create_user(db, user=request.parameter)
    if(x==False):
        return Response(status="Ok",
                    code="200",
                    message="Email already exists").dict(exclude_none=True)
    
    return Response(status="Ok",
                    code="200",
                    message="Signed up successfully",result=x).dict(exclude_none=True)

@router.get("/")
async def start():
    return Response(message="hello",status="OK",code="200")
@router.get("/getAll")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = crud.get_user(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)


@router.delete("/delete")
async def delete_user(request: RequestUser,  db: Session = Depends(get_db)):
    crud.remove_user(db, user_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

@router.post("/login")
async def login_user(request: RequestUser, db: Session = Depends(get_db)):
    x = crud.login(db,user=request.parameter)
    if(x==False):
        return Response(status="Ok", code="200",message="incorrect email or password").dict(exclude_none=True)
    return Response(status="Ok", code="200", message="user logged in",result=x).dict(exclude_none=True)