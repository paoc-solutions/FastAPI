import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Club as SchemaClub
from schema import User as SchemaUser

from models import Club as ModelClub
from models import User as ModelUser

import os
from dotenv import load_dotenv

load_dotenv(".env")


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/club", response_model=SchemaClub)
async def club(club: SchemaClub):
    db_club = ModelClub(
        name=club.name, description=club.description, address=club.address
    )
    db.session.add(db_club)
    db.session.commit()
    return db_club


@app.get("/club")
async def club():
    clubs = db.session.query(ModelClub).all()
    return clubs


@app.post("/user", response_model=SchemaUser)
async def user(user: SchemaUser):
    db_user = ModelUser(name=user.name, birth=user.birth)
    db.session.add(db_user)
    db.session.commit()
    return db_user


@app.get("/user")
async def user():
    users = db.session.query(ModelUser).all()
    return users


# To run locally
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
