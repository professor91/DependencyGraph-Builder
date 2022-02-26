import os
from json_db import jsdb
from headerParser import parser

db= jsdb("./data.json")

def makeFileSystem(dirName: str):
    fs= {}
    for item in os.listdir(dirName):
        if os.path.isfile(dirName+item):
            fs[item]= "file"
        else:
            fs[dirName+item]= makeFileSystem(dirName+item+"/")
    return fs

db._cacheddata= makeFileSystem("./src/")
db.dumpdata()

x= parser("./src/dpp/application.cpp")
x.getHeaders()
