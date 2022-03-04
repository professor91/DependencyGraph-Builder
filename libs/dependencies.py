#   Dependency Graph Builder

import os

from libs.headerParser import parser
from libs.json_db import jsdb

class depGraphBuilder:
    def __init__(self, dirPath: str):
        self.db_dp= jsdb("./cache/dependencies.json")
        self.db_cdp= jsdb("./cache/calc_dependency.json")

        self.db_dp._cacheddata= self.makeDependencyDict(dirPath)
        self.db_dp.dumpdata()

    #   Build a dictionary with
    #       key:    fileName
    #       value:  name of dependencies
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

    #   Build a dictionary with
    #       key:    fileName
    #       value:  number of dependencies
    def calcDependency(self, dep_dict: dict):
        # for each file
        for key in dep_dict.keys():
            # if file is directory make recursive call
            if type(dep_dict[key]) is dict:
                self.calcDependency(dep_dict[key])
            # calculate on how many files it depends
            else:
                self.db_cdp._cacheddata[key]= len(dep_dict[key])

        self.db_cdp.dumpdata()
