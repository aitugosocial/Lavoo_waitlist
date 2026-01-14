from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Waitlist(Base):
    """
    Waitlist table to store email addresses of users waiting for the application launch.
    """
    __tablename__ = "waitlist"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"<Waitlist(id={self.id}, email={self.email}, created_at={self.created_at})>"
