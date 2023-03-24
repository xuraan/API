from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base

class Version(Base):
    __tablename__ = "versions"
    id = Column(String, primary_key=True)

    created_date = Column(DateTime, default=datetime.utcnow)
    last_modified_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    descriptions = relationship("VersionDescription", back_populates="version")



class VersionDescription(Base):
    __tablename__ = "versions_description"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    language = Column(String)
    version_id = Column(String, ForeignKey("versions.id"), index=True)

    created_date = Column(DateTime, default=datetime.utcnow)
    last_modified_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    version = relationship("Version", back_populates="descriptions")


class Local(Base):
    __tablename__ = "locals"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    flag = Column(String)


class Question(Base):
    __tablename__ = "questions"
    id = Column(String, primary_key=True)
    text = relationship("LocalizedQuestion", back_populates="question")

class LocalizedQuestion(Base):
    __tablename__ = "questions_localized"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    language = Column(String)
    question_id = Column(String, ForeignKey("questions.id"), index=True)

    created_date = Column(DateTime, default=datetime.utcnow)
    last_modified_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    question = relationship("Question", back_populates="text")


class Answer(Base):
    __tablename__ = "answers"
    id = Column(String, primary_key=True)
    src = Column(String)
    text = relationship("LocalizedAnswer", back_populates="answer")


class LocalizedAnswer(Base):
    __tablename__ = "answers_localized"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    language = Column(String)
    answer_id = Column(String, ForeignKey("answers.id"), index=True)

    created_date = Column(DateTime, default=datetime.utcnow)
    last_modified_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    answer = relationship("Answer", back_populates="text")




    