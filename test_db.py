from sqlalchemy import create_engine, text

# Make sure this matches your Docker/Postgres setup
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/workflow_db"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Try a simple query
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Database connection successful, result:", result.fetchone())
except Exception as e:
    print("Database connection failed!")
    print(e)