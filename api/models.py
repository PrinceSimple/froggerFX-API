from typing import List
from pydantic import BaseModel

class Player(BaseModel):
    name: str
    highscore: int