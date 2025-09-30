from fastapi import FastAPI , Request

from pymongo import MongoClient




app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static") #all static files are being served from static folder
templates = Jinja2Templates(directory="templates") #the template is in the templates directory
conn = MongoClient("mongodb+srv://prakirtibista7:Bunuchhetry2@cluster0.egseduj.mongodb.net/")


    



