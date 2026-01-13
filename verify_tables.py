from sqlalchemy import create_engine, inspect

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/workflow_db")
inspector = inspect(engine)
print(inspector.get_table_names())