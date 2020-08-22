import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import Publisher, Book

DB_PATH = 'postgresql+psycopg2://postgres:maximus@localhost:5432/Book_shop'
engine = sq.create_engine(DB_PATH)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

if __name__ == '__main__':
    session = Session()
    all_shops = session.query(Book).all()
    print(all_shops)

