from fastapi import FastAPI,status, Depends, HTTPException
from typing import List,Annotated
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models

from .db_conn import engine,SessionLocal
from . import auth

app  = FastAPI()
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

db_dependency = Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(auth.get_current_user)]

@app.get('/',status_code=status.HTTP_200_OK)
async def user(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    return {"User": user}