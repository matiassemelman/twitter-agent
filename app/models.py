from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base

class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    tweet_id = Column(String, unique=True, index=True)
    content = Column(String)
    created_at = Column(DateTime)
    processed = Column(Boolean, default=False)
    is_tip = Column(Boolean, default=False)
