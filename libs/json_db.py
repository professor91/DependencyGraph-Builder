import json

# class for handeling josn files
class jsdb:
    #0. constructor
    def __init__(self, _fileName: str):
        self._cacheddata= {}
        self.fileName= _fileName
        self.reload()

    #1. dump data in json file
    def dumpdata(self):
        with open(self.fileName, "w") as wf:
            json.dump(self._cacheddata, wf, indent=4)
        self.reload()

    #2. reload data from json file
    def reload(self):
        with open(self.fileName, "r") as rf:
            self._cacheddata= json.load(rf)

    #3. add key val to the db
    def addItem(self, key: str, value: str):
        self._cacheddata[key]= value
        self.dumpdata()