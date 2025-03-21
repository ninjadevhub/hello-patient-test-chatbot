from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate,UserCreate
from fastapi import HTTPException
import httpx
import os
import openai
from sqlalchemy import func
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")

openai.api_key = OPENAI_API_KEY  # Set OpenAI API key

def get_items(db: Session):
    return db.query(User).all()



def update_thread_data(db: Session, email: str, user: UserCreate):
    # Retrieve the existing user from the database
    db_user = db.query(User).filter(User.email == email).first()
    
    if db_user:

        db_user.thread_data = user['thread_data']
        # Commit the changes to the database
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return None  # or raise an exception if you prefer


    
async def generate_text(db: Session, user: UserCreate):
    thread_data =  db.query(User).filter(User.email == user.email).first().thread_data

    if thread_data is not None:
         thread_data.append({'role': 'user', 'content': user.prompt})
    else:
            # If thread_data is None (not set), initialize it as a new list
        thread_data = [{'role': 'user', 'content': user.prompt}]     
    """
    Generate text response from OpenAI's GPT model based on a user-provided prompt.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
            messages=[{'role': 'user', 'content': user.prompt}],
            temperature=0.7
        )
        assistant_reply = response["choices"][0]["message"]["content"]

        thread_data.append({'role': 'assistant', 'content': assistant_reply})
        update_thread_data(db, user.email, {'thread_data': thread_data})
        return {"response": assistant_reply}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")  

def get_history_by_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first().thread_data    


