from fastapi import FastAPI
from ..models.artistsModel import ArtistModel
from ..schema.artistsSchema import Artist
from sqlalchemy.orm import Session

artistRouter = FastAPI()


@artistRouter.get('/artist/', response_model=list(Artist))
async def get_artist(db: Session = Depends(get_db), skip: int = 0):
    artist = db.query(ArtistModel).offset(skip).all()
    return artist

@artistRouter.get('/artist/')
async def get_artist(db: Session, skip: int = 0):
    artist = db.query(ArtistModel).offset(skip).all()
    return artist
