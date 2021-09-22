import os

from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property


db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    thumbnail = db.relationship(
        "Thumbnail", backref="item",
        cascade="all, delete-orphan", uselist=False
    )

    @hybrid_property
    def remove_thumbnail(self):
        try:
            if self.thumbnail:
                os.remove(
                    os.path.join(
                        current_app.config['MEDIA_FOLDER'],
                        self.thumbnail.unique_name)
                )
        except OSError:
            pass

    def __unicode__(self):
        return unicode(self.name).encode('utf-8')

    def __repr__(self):
        return self.__unicode__()


class Thumbnail(db.Model):
    __tablename__ = 'thumbnails'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    unique_name = db.Column(db.Unicode, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    def __unicode__(self):
        return unicode(self.unique_name).encode('utf-8')

    def __repr__(self):
        return self.__unicode__()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    email = db.Column(db.Unicode, nullable=False)
