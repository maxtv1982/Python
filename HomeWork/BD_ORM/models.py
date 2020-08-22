import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Publisher (Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    books = relationship('Book', backref='publisher')


class Book (Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    id_publisher = sq.Column(sq.ForeignKey('publisher.id'))
