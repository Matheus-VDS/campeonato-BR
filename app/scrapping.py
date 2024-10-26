import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://api-football-v1.p.rapidapi.com/v3"
headers = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': "api-football-v1.p.rapidapi.com"}

async def fetch_past_games(team_id: int):
    async with aiohttp.ClientSession() as session:
        url = f"{BASE_URL}/fixtures?team={team_id}&season=2023"
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            return data["response"]

async def fetch_future_games(team_id: int):
    async with aiohttp.ClientSession() as session:
        url = f"{BASE_URL}/fixtures?team={team_id}&status=NS"
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            return data["response"]
