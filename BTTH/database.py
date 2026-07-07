from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:020206002751localhost:3306/ecommerce_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,  
    autoflush=False,    
    bind=engine         
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()