import uvicorn
from fastapi import FastAPI
from sqlalchemy import DBSessionMiddleware, db
import os
from dotenv import load_dotenv
from starlette.responses import RedirectResponse

from schema.artistsSchema import Artist
from models.artistsModel import ArtistModel
from routes.artists import artistRouter

from schema.usersSchema import User
from models.usersModel import UserModel
from routes.users import userRouter

from schema.festivalsSchema import Festival
from models.festivalsModel import FestivalModel
from routes.festivals import festivalRouter

from schema.sessionsSchema import Session
from models.sessionsModel import SessionModel
from routes.sessions import sessionRouter

load_dotenv('.env')
FestivalUserAPI = FastAPI()

FestivalUserAPI.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


# FestivalUserAPI.include_router(artistRouter, tags=["Artist routes"])
# FestivalUserAPI.include_router(festivalRouter, tags=["Festival routes"])
# FestivalUserAPI.include_router(userRouter, tags=["User routes"])
# FestivalUserAPI.include_router(sessionRouter, tags=["Session routes"])


@FestivalUserAPI.get("/")
async def read_route():
    response = RedirectResponse(url='/docs')
    return response


@FestivalUserAPI.get('/artist/')
async def artist():
    return db.session.query(ArtistModel).all()


@FestivalUserAPI.get('/artist/')
async def artist():
    return db.session.query(ArtistModel).all()


if __name__ == '__main__':
    uvicorn.run(FestivalUserAPI, host='0.0.0.0', port=8000)
