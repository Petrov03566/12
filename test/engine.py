from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://postgres:univer@localhost/da")
session = Session(bind=engine)