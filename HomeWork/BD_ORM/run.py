import sqlalchemy as sq
import json
from sqlalchemy.orm import sessionmaker
from models_DB import Publisher, Book, Sale, Shop, Stock, Base

DB_PATH = 'postgresql://postgres:maximus@localhost:5432/Book_shop'
engine = sq.create_engine(DB_PATH)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

if __name__ == '__main__':
    session = Session()
    with open('tests_data.json', encoding="utf-8") as f:
        json_data = json.load(f)
    for item in json_data:
        table = item["model"].capitalize()
        if table == 'Publisher':
            info = Publisher(id=item["pk"])
            print(1)
            session.add(info)
            session.query(Publisher).filter(Publisher.id == item["pk"]).update(item["fields"])
            session.commit()
        elif table == 'Shop':
            info = Shop(id=item["pk"])
            print(2)
            session.add(info)
            session.query(Shop).filter(Shop.id == item["pk"]).update(item["fields"])
            session.commit()
        elif table == 'Book':
            info = Book(id=item["pk"])
            print(3)
            session.add(info)
            session.query(Book).filter(Book.id == item["pk"]).update(item["fields"])
            session.commit()
        elif table == 'Stock':
            info = Stock(id=item["pk"])
            print(4)
            session.add(info)
            session.query(Stock).filter(Stock.id == item["pk"]).update(item["fields"])
            session.commit()
        elif table == 'Sale':
            info = Sale(id=item["pk"])
            print(5)
            session.add(info)
            session.query(Sale).filter(Sale.id == item["pk"]).update(item["fields"])
            session.commit()



