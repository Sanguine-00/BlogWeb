# coding: utf-8
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class AdminInfo(db.Model):
    __tablename__ = 'admin_info'

    db_id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.String(40), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.BigInteger, nullable=False)
    last_login_time = db.Column(db.BigInteger)


class BlogInfo(db.Model):
    __tablename__ = 'blog_info'

    db_id = db.Column(db.Integer, primary_key=True)
    catalog_id = db.Column(db.ForeignKey('catalog_info.catalog_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    blog_id = db.Column(db.String(40), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.String(255))
    content = db.Column(db.String)
    publish_time = db.Column(db.BigInteger)
    modify_time = db.Column(db.BigInteger)
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())

    catalog = db.relationship('CatalogInfo', primaryjoin='BlogInfo.catalog_id == CatalogInfo.catalog_id', backref='blog_infos')


class CatalogInfo(db.Model):
    __tablename__ = 'catalog_info'

    db_id = db.Column(db.Integer, primary_key=True)
    catalog_id = db.Column(db.String(40, 'utf8_general_ci'), nullable=False, index=True)
    name = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    column_id = db.Column(db.ForeignKey('column_info.column_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    column = db.relationship('ColumnInfo', primaryjoin='CatalogInfo.column_id == ColumnInfo.column_id', backref='catalog_infos')


class ColumnInfo(db.Model):
    __tablename__ = 'column_info'

    db_id = db.Column(db.Integer, primary_key=True)
    column_id = db.Column(db.String(40), nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False)
