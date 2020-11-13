from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgres://emvhsuwtpkppmp:697138f9b8c13970147e808aa752912ea41d9f8105252f8d346c52008a3281c7@ec2-46-137-124-19.eu-west-1.compute.amazonaws.com:5432/dc6cha0mimkbrs'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

players = Table(
    'players',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('highscore', Integer),
)

database = Database(DATABASE_URL)
