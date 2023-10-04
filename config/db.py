from pymongo import MongoClient
conn = MongoClient("mongodb+srv://nghiemptce160353:eXhTjDVk2nxwXSnz@cluster0.of86fvh.mongodb.net/digital_library")
database = conn.get_database()