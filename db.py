from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base  

DATABASE_URL = 'sqlite:///scheduler.db' 

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(bind=engine)

def initialize_db():
    """Initialize the database by creating all tables."""
    Base.metadata.create_all(engine)
