from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .database import SessionLocal, init_db
from . import crud, schemas

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/teams/", response_model=schemas.Team)
async def create_team(team: schemas.TeamCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_team(db=db, team=team)

@app.post("/games/", response_model=schemas.Game)
async def create_game(game: schemas.GameCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_game(db=db, game=game)

@app.get("/teams/", response_model=List[schemas.Team])
async def read_teams(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_teams(db=db)

@app.get("/games/{game_id}", response_model=schemas.Game)
async def read_game(game_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_game_by_id(db=db, game_id=game_id)

@app.get("/teams/{team_id}/players", response_model=List[schemas.Player])
async def read_players(team_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_players_by_team(db=db, team_id=team_id)

