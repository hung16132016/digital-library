from fastapi import APIRouter
from models.user import User
from config.db import conn
from config.db import database
from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter()


@user.get('/')
async def find_all_users():
    return serializeList(database.user.find())


@user.get('/{id}')
async def find_one_user(id):
    return serializeDict(database.user.find_one({"_id": ObjectId(id)}))


@user.post('/')
async def create_user(user: User):
    database.user.insert_one(dict(user))
    return serializeList(database.user.find())


@user.put('/{id}')
async def update_user(id, user: User):
    database.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return serializeDict(database.user.find_one({"_id": ObjectId(id)}))


@user.delete('/{id}')
async def delete_user(id, user: User):
    return serializeDict(database.user.find_one_and_delete({"_id": ObjectId(id)}))
