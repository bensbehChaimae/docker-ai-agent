import os 

import sqlmodel 
from sqlmodel import Session, SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")

# Check if the DATABASE_URL environment variable is set
if DATABASE_URL is None:
    raise NotImplementedError("`Database_URL` was not set")


# Create the SQLModel engine using the provided database URL
engine = sqlmodel.create_engine(DATABASE_URL)


# Database model : 
# Do not create db migrations 
def init_db():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)



# Function to get a session for database operations
# useful for api routes
def get_session() :
    # Create a new session using the engine
    with Session(engine) as session:
        # Yield the session to be used in the context of a request
        yield session 