from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Schema para o time
class TeamBase(BaseModel):
    name: str
    rank: Optional[int]
    championships: List[str]

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        from_attributes = True  # Mudar 'orm_mode' para 'from_attributes'

# Schema para o jogo
class GameBase(BaseModel):
    team_home_id: int
    team_away_id: int
    score_home: Optional[int]
    score_away: Optional[int]
    stadium: Optional[str]
    championship: Optional[str]
    date: datetime
    referee: Optional[str]

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int

    class Config:
        from_attributes = True  # Mudar 'orm_mode' para 'from_attributes'

# Schema para o jogador
class PlayerBase(BaseModel):
    name: str
    team_id: int

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int

    class Config:
        from_attributes = True  # Mudar 'orm_mode' para 'from_attributes'
