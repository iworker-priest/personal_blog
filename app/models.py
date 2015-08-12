# -*- coding: utf-8 -*-

from . import db 

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(64), unique=True)

    def add_tag(self):
        tag = Tag.query.filter_by(tag_name=r).first()
        if tag is None:
            db.session.add(self)
            db.session.commit()
            return True
        return False

class Archive(db.Model):
    __tablename__ = 'archives'
    id = db.Column(db.Integer, primary_key=True)
    archive_title = db.Column(db.Unicode(128), unique=True)

class Tag_Archive(db.Model):
    __tablename__ = 'tags_archives'
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, index=True)
    archive_id = db.Column(db.Integer, index=True)