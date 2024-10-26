from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.future import select


# Função para criar um novo time
async def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    await db.commit()
    await db.refresh(db_team)
    return db_team


# Função para criar um novo jogo
async def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    await db.commit()
    await db.refresh(db_game)
    return db_game


# Função para listar todos os times
async def get_all_teams(db: AsyncSession):
    result = await db.execute(select(models.Team))
    return result.scalars().all()

# Função para buscar um jogo específico pelo ID
async def get_game_by_id(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()


# Função para listar jogadores de um time
async def get_players_by_team(db: AsyncSession, team_id: int):
    result = await db.execute(select(models.Player).where(models.Player.team_id == team_id))
    return result.scalars().all()

