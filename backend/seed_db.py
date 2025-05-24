# backend/seed_db.py

from backend.src.database import SessionLocal
from backend.src.models import User, Developer
from backend.src.utils import hash_password

db = SessionLocal()

try:
    # Seed one developer
    dev = Developer(
        full_name="Jane Developer",
        company="Dev Co",
        email="jane@devco.com",
        portfolio="https://devco.com",
        password=hash_password("securedev123")
    )

    # Seed one user
    user = User(
        full_name="John User",
        username="johnuser",
        email="john@example.com",
        password=hash_password("secureuser123")
    )

    db.add_all([dev, user])
    db.commit()

    print("🌱 Seed data inserted successfully.")

finally:
    db.close()
