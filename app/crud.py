import email
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserSchema
 

def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def login(db: Session, user: UserSchema):
    q = db.query(User).filter(User.email == user.email, User.password==user.password).first()
    if(q):
        return q
    return False

def create_user(db: Session, user: UserSchema):
    query = db.query(User).filter(User.email==user.email).first()
    if(query):
        return False
    _user = User(name=user.name,email=user.email,password=user.password)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()


def update_user(db: Session, user_id: int, name: str, email: str, password: str):
    _user = get_user_by_id(db=db, user_id=user_id)

    _user.name = name
    _user.email = email
    _user.password = password
    db.commit()
    db.refresh(_user)
    return _user