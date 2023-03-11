from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field
from datetime import datetime

engine = create_engine('sqlite:///test.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class UserSession(Base):
    __tablename__ = 'user_sessions'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ip = Column(String)
    username = Column(String)
    chat_id = Column(Integer, autoincrement=True)
    start_time = Column(DateTime, default=datetime.utcnow())
    chat_messages = relationship('ChatMessage', back_populates='user_session')


class ChatMessage(Base):
    __tablename__ = 'chat_messages'

    id = Column(Integer, primary_key=True, index=True)
    user_session_id = Column(Integer, ForeignKey('user_sessions.id'))
    agent = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow())
    user_session = relationship('UserSession', back_populates='chat_messages')


class UserSessionIn(BaseModel):
    ip: str = Field(...)
    username: str = Field(...)
    chat_id: int = Field(...)


class UserSessionOut(BaseModel):
    id: int = Field(...)
    ip: str = Field(...)
    username: str = Field(...)
    chat_id: int = Field(...)
    start_time: datetime = Field(...)


class ChatMessageIn(BaseModel):
    user_session_id: int = Field(...)
    message: str = Field(...)


class ChatMessageOut(BaseModel):
    id: int = Field(...)
    user_session_id: int = Field(...)
    message: str = Field(...)
    timestamp: datetime = Field(...)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_single_db():
    return next(get_db())

def create_user_session(db, user_session: UserSessionIn):
    db_user_session = UserSession(**user_session.dict())
    db.add(db_user_session)
    db.commit()
    db.refresh(db_user_session)
    return UserSessionOut(**db_user_session.__dict__)


def create_chat_message(db, chat_message: ChatMessageIn, agent: str = 'user'):
    db_chat_message = ChatMessage(**chat_message.dict(), agent=agent)
    db.add(db_chat_message)
    db.commit()
    db.refresh(db_chat_message)
    return ChatMessageOut(**db_chat_message.__dict__)

def get_user_session(db, user_session_id: int):
    user_session = db.query(UserSession).filter(UserSession.id == user_session_id).first()
    return UserSessionOut(**user_session.__dict__)
