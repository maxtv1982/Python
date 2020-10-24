import sqlalchemy as sq
import json
from sqlalchemy.orm import sessionmaker
from base_table import User, DatingUser, Photo

DB_PATH = 'postgresql://postgres:maximus@localhost:5432/Dating_base'
engine = sq.create_engine(DB_PATH)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

session = Session()


def import_data(user_info):
    """  заполняем таблицу о пользователях заданными параметрами"""
    vk_id = User(vk_id=user_info['vk_id'])
    session.add(vk_id)
    first_name = User(first_name=user_info['first_name'])
    session.add(first_name)
    last_name = User(last_name=user_info['last_name'])
    session.add(last_name)
    age = User(age=user_info['age'])
    session.add(age)
    sex = User(sex=user_info['sex'])
    session.add(sex)
    city = User(city=user_info['city'])
    session.add(city)
    session.commit()

def import_data(user_info):
    """  заполняем таблицу найденных пары для пользователя заданными параметрами"""
    vk_id = User(vk_id=user_info['vk_id'])
    session.add(vk_id)
    first_name = User(first_name=user_info['first_name'])
    session.add(first_name)
    last_name = User(last_name=user_info['last_name'])
    session.add(last_name)
    age = User(age=user_info['age'])
    session.add(age)
    sex = User(sex=user_info['sex'])
    session.add(sex)
    city = User(city=user_info['city'])
    session.add(city)
    session.commit()