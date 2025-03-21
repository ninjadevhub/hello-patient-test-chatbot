from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User  # Import your models
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Setup database connection and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Add initial data to the User table
def seed_data():
    users = [
        User(name="John Doe", email="john@example.com", password="hashedpassword1", thread_id=""),
    ]
    session.add_all(users)
    session.commit()

if __name__ == "__main__":
    seed_data()
    print("Seed data inserted!")
