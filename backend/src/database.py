# backend/src/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the DATABASE_URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Validate it's set
if not DATABASE_URL:
    raise ValueError(
        "❌ DATABASE_URL is not set in environment. Check your .env file.")

# Fix Heroku's legacy scheme
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Create SQLAlchemy engine with SSL requirement (Heroku)
engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})

# Create session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for ORM models
Base = declarative_base()
