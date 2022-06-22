import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from .models.artistsModel import ArtistModel
from .models.usersModel import UserModel
from .models.festivalsModel import FestivalModel

from .schema.artistsSchema import ArtistBase as ArtisteSchema
from .schema.usersSchema import UserBase as UserSchema
from .schema.festivalsSchema import FestivalBase as FestivalSchema

from .database import get_session

FestivalUserAPI = FastAPI()

db = get_session()


# Redirect to docs
@FestivalUserAPI.get("/")
async def read_route():
    response = RedirectResponse(url='/docs')
    return response


# Artistes
@FestivalUserAPI.post("/artiste", response_model=ArtisteSchema)
async def artist(artiste: ArtisteSchema):
    db_artiste = ArtistModel(firstname=artiste.firstname, name=artiste.name, style=artiste.style)
    db.session.add(db_artiste)
    db.session.commit()
    return db_artiste


@FestivalUserAPI.get("/artist/{id}", response_model=ArtisteSchema)
async def artist(id: int):
    artist = ArtistModel.get(id)
    return artist


@FestivalUserAPI.get('/artists')
async def artist():
    artist = db.session.query(ArtistModel).all()
    return artist


# Users
@FestivalUserAPI.post("/user", response_model=UserSchema)
async def user(user: UserSchema):
    db_user = UserModel(email=user.email, password=user.password)
    db.session.add(db_user)
    db.session.commit()
    return db_user


@FestivalUserAPI.get("/user/{id}", response_model=UserSchema)
async def user(id: int):
    user = UserModel.get(id)
    return user


@FestivalUserAPI.get('/users')
async def user():
    user = db.session.query(UserModel).all()
    return user


# Festival
@FestivalUserAPI.post("/festival", response_model=FestivalSchema)
async def festival(festival: FestivalSchema):
    db_festival = FestivalModel(name=festival.name, city=festival.city, zipcode=festival.zipcode,
                                address=festival.address)
    db.session.add(db_festival)
    db.session.commit()
    return db_festival


@FestivalUserAPI.get("/festival/{id}", response_model=FestivalSchema)
async def festival(id: int):
    festival = FestivalModel.get(id)
    return festival


@FestivalUserAPI.get('/festivals')
async def festival():
    festival = db.session.query(FestivalModel).all()
    return festival


if __name__ == '__main__':
    uvicorn.run(FestivalUserAPI, host='127.0.0.1', port=8000)
