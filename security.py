import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

print("Applying security roles")
with engine.begin() as conn:
    with open('security_setup.sql', 'r') as file:
        conn.execute(text(file.read()))
print(" Internal Security Complete")