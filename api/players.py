from typing import List
from fastapi import Header, APIRouter

from api.models import Player

fake_player_db = [
  {
    'name': 'Frank',
    'highscore': 65536
  }
]

players = APIRouter()

@players.get('/', response_model=List[Player])
async def index():
  return fake_player_db
