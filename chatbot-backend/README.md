# FastAPI Application with PostgreSQL and Alembic

This is a FastAPI application using PostgreSQL as the database and Alembic for database migrations.

## Prerequisites

Ensure you have the following installed:
- Python (>=3.8)
- PostgreSQL
- Virtual environment (optional but recommended)

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Create and activate a virtual environment

**For macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**For Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root and set the following variables:
```
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```
Replace `username`, `password`, and `database_name` with your PostgreSQL credentials.

### 5. Apply database migrations
```bash
alembic upgrade head
```

### 6. Seed the database (if applicable)
```bash
python seed.py
```

### 7. Run the application
```bash
uvicorn main:app --reload
```

## Project Structure
```
.
├── app
│   ├── main.py  # FastAPI application entry point
│   ├── models.py  # SQLAlchemy models
│   ├── schemas.py  # Pydantic schemas
│   ├── routes  # API route handlers
│   ├── database.py  # Database connection
│   ├── services.py  # Business logic
├── alembic  # Alembic migration scripts
├── seed.py  # Database seeding script
├── requirements.txt  # Python dependencies
├── .env  # Environment variables
```

## Useful Commands

### Run the application
```bash
uvicorn main:app --reload
```

### Apply latest migrations
```bash
alembic upgrade head
```

### Seed the database
```bash
python seed.py
```

### Activate virtual environment

**For macOS/Linux:**
```bash
source venv/bin/activate
```

**For Windows:**
```powershell
venv\Scripts\activate
```

### Create a new Alembic migration
```bash
alembic revision --autogenerate -m "Migration message"
```

### Deactivate virtual environment
```bash
deactivate
```

## License
[Specify License Here]

