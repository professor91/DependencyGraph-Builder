#   Dependency Graph Builder
#   Build a dictionary with
#       key:    fileName
#       value:  dependencies

import os

from libs.headerParser import parser
from libs.json_db import jsdb

class depGraphBuilder:
    def __init__(self, dirPath: str):
        self.db_dp= jsdb("./cache/dependencies.json")

        self.db_dp._cacheddata= self.makeDependencyDict(dirPath)
        self.db_dp.dumpdata()

    def makeDependencyDict(self, dirName: str):
        dp= {}
        for item in os.listdir(dirName):
            # if file then parse it
            if os.path.isfile(dirName+item):
                x= parser(dirName+item)
                x.getHeaders()
                dp[item]= x.headers
            # if directory then make recursive call
            else:
                dp[dirName+item]= self.makeDependencyDict(
                                                        dirName+item+"/")
        
        return dp
