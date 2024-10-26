from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    rank = Column(Integer)

    home_games = relationship("Game", foreign_keys='Game.team_home_id', back_populates="team_home")
    away_games = relationship("Game", foreign_keys='Game.team_away_id', back_populates="team_away")


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, index=True)
    team_home_id = Column(Integer, ForeignKey('teams.id'))
    team_away_id = Column(Integer, ForeignKey('teams.id'))
    score_home = Column(Integer)
    score_away = Column(Integer)
    stadium = Column(String)
    championship = Column(String)
    date = Column(DateTime)
    referee = Column(String)

    team_home = relationship("Team", foreign_keys=[team_home_id], back_populates="home_games")
    team_away = relationship("Team", foreign_keys=[team_away_id], back_populates="away_games")
    cards = relationship("Card", back_populates="game")
    injuries = relationship("Injury", back_populates="game")
    performances = relationship("Performance", back_populates="game")


class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team_id = Column(Integer, ForeignKey('teams.id'))

    performances = relationship("Performance", back_populates="player")
    team = relationship("Team")


class Performance(Base):
    __tablename__ = 'performances'
    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    player_id = Column(Integer, ForeignKey('players.id'))
    goals = Column(Integer)
    assists = Column(Integer)
    shots = Column(Float)
    passes = Column(Float)
    tackles = Column(Float)

    game = relationship("Game", back_populates="performances")
    player = relationship("Player", back_populates="performances")


class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    player_id = Column(Integer, ForeignKey('players.id'))
    card_type = Column(String)

    game = relationship("Game", back_populates="cards")
    player = relationship("Player")


class Injury(Base):
    __tablename__ = 'injuries'
    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    player_id = Column(Integer, ForeignKey('players.id'))
    injury_type = Column(String)

    game = relationship("Game", back_populates="injuries")
    player = relationship("Player")
