from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgres://vwdyhgumygnsxk:fef79760d291bbd747340e22add96213cbb7481ae16405846d7ede6245358801@ec2-54-166-114-48.compute-1.amazonaws.com:5432/da5v13renqim89'

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