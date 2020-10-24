import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    """ вся информация по пользователю """
    __tablename__ = 'user'
    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    age = sq.Column(sq.Integer)
    age_from = sq.Column(sq.Integer)
    age_to = sq.Column(sq.Integer)
    sex = sq.Column(sq.String)
    city = sq.Column(sq.String)
    dating_users = relationship('DatingUser', backref='user', cascade='all, delete-orphan')


class DatingUser(Base):
    """ Найденные пары для пользователя """
    __tablename__ = 'dating_user'
    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    age = sq.Column(sq.Integer)
    id_user = sq.Column(sq.ForeignKey('user.id', ondelete='CASCADE'))
    photos = relationship("Photo", backref='dating_user', cascade='all, delete-orphan')


class Photo(Base):
    """ Фотографии найденных пар """
    __tablename__ = 'photo'
    id = sq.Column(sq.Integer, primary_key=True)
    id_dating_user = sq.Column(sq.ForeignKey('dating_user.id', ondelete='CASCADE'))
    link_photo = sq.Column(sq.String)
    count_likes = sq.Column(sq.Integer)


