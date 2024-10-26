import sys
import os

# Adiciona o caminho do projeto à variável de sistema
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

# Crie uma sessão com o banco de dados
db = SessionLocal()

# Função para inserir times
def insert_teams():
    teams_to_add = [
        schemas.TeamCreate(name="Flamengo", rank=1, championships=["Campeonato Brasileiro", "Libertadores"]),
        schemas.TeamCreate(name="Palmeiras", rank=2, championships=["Campeonato Brasileiro", "Copa do Brasil"]),
        schemas.TeamCreate(name="São Paulo", rank=3, championships=["Campeonato Brasileiro", "Libertadores"]),
        schemas.TeamCreate(name="Santos", rank=4, championships=["Campeonato Brasileiro", "Copa do Brasil"])
    ]

    for team in teams_to_add:
        crud.create_team(db=db, team=team)

# Execute a inserção de times
if __name__ == "__main__":
    insert_teams()
    print("Times inseridos com sucesso!")
    db.close()

