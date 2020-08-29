import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    books = relationship('Book', backref='publisher', cascade='all, delete-orphan')


class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    stock = relationship("Stock", backref='book', cascade='all, delete-orphan')
    id_publisher = sq.Column(sq.ForeignKey('publisher.id', ondelete='CASCADE'))


class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    stocks = relationship("Stock", backref='shop', cascade='all, delete-orphan')


class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.ForeignKey('book.id', ondelete='CASCADE'))
    id_shop = sq.Column(sq.ForeignKey('shop.id', ondelete='CASCADE'))
    count = sq.Column(sq.Integer)
    sales = relationship("Sale", backref='stock', cascade='all, delete-orphan')


class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.ForeignKey('stock.id', ondelete='CASCADE'))
    count = sq.Column(sq.Integer)






