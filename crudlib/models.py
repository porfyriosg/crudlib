from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, validates
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    """
    User model representing a user in the database.

    Attributes:
        id (int): Primary key.
        name (str): Name of the user.
        email (str): Email of the user.
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement="auto", index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    inserted = Column(DateTime(timezone=True), nullable=True, server_default=func.now())
    updated = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    status = Column(Integer, nullable=True)

# Add more models as needed
