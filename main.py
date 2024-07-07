from fastapi import FastAPI,status,Depends,HTTPException
import models
from database import engine,SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
import auth
from auth import get_current_user

app = FastAPI()
app.include_router(auth.router)


models.Base.metadata.create_all(bind=engine) # inite base database 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]

@app.get("/get_user",status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User Not Found")
    
    return{"user":user}