from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, database, service, schemas
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
origins = [
    "*",  # Allow all domains (use with caution)
]

# Add CORSMiddleware to handle CORS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with PostgreSQL!"}

@app.get("/get-history-by-user/{user_email}")
def create_item(user_email: str, db: Session = Depends(database.get_db)):
    return service.get_history_by_user(db, user_email)




@app.post("/generate-text/")
async def generate_text(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return await service.generate_text(db, user)