from fastapi import APIRouter
from config.db import *
from models.index import users
from schemas.index import users
addressbook = APIRouter()
 
@addressbook.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@addressbook.get("/{id}")
async def read_data(id : int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@addressbook.post("/")
async def write_data(addressbook : users):
    conn = conn.execute(users.insert().values(
        Name = addressbook.Name,
        Email = addressbook.Email,
        Address = addressbook.Address,
        Pincode = addressbook.Pincode
    ))
    return conn.execute(users.select()).fetchall()

@addressbook.put("/{id}")
async def update_data(id : int, addressbook:users):
    conn = conn.execute(users.update().values(
        Name = addressbook.Name,
        Email = addressbook.Email,
        Address = addressbook.Address,
        Pincode = addressbook.Pincode
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()
    

@addressbook.delete("/")
async def delete_data(id : int, addressbook:users):
    conn = conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

