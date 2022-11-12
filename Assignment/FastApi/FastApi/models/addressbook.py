from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String
from config.db import meta,engine

users = Table(
    'addressbook', meta, 
    Column("id", Integer, primary_key=True),
    Column('Name', String(255)),
    Column('Email',String(255)),
    Column('Address',String(255)),
    Column('Pincode',Integer)
)
meta.create_all(engine)