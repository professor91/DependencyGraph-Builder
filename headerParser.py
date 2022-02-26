class parser():
    def __init__(self, fileName: str):
        self.fileName= fileName
        self.headers= []
    
    def getHeaders(self):
        rf = open(self.fileName, 'r')
        lines = rf.readlines()

        for line in lines:
            if "#include" in line:
                print(line.strip("\n#include>"))
