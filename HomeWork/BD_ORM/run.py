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


    def import_data(file):
        with open(file, encoding="utf-8") as f:
            json_data = json.load(f)
        for item in json_data:
            table = item["model"].capitalize()
            if table == 'Publisher':
                info = Publisher(id=item["pk"])
                session.add(info)
                session.query(Publisher).filter(Publisher.id == item["pk"]).update(item["fields"])
                session.commit()
            elif table == 'Shop':
                info = Shop(id=item["pk"])
                session.add(info)
                session.query(Shop).filter(Shop.id == item["pk"]).update(item["fields"])
                session.commit()
            elif table == 'Book':
                info = Book(id=item["pk"])
                session.add(info)
                session.query(Book).filter(Book.id == item["pk"]).update(item["fields"])
                session.commit()
            elif table == 'Stock':
                info = Stock(id=item["pk"])
                session.add(info)
                session.query(Stock).filter(Stock.id == item["pk"]).update(item["fields"])
                session.commit()
            elif table == 'Sale':
                info = Sale(id=item["pk"])
                session.add(info)
                session.query(Sale).filter(Sale.id == item["pk"]).update(item["fields"])
                session.commit()


    #import_data('tests_data.json')
    publisher_info = input('введите имя издателя: ')
    shops = session.query(Shop).join(Stock, Stock.id_shop == Shop.id).join(Book, Book.id == Stock.id_book)\
        .join(Publisher, Publisher.id == Book.id_publisher).filter(Publisher.name == publisher_info).all()
    if len(shops) != 0:
        for shop in shops:
            print(shop.name)
    else:
        print('книг такого издателя в продаже нет')

