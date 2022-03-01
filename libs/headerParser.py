#   Parser
#   Parser class accepts a source code file
#   list all the headers in a pre-defined format

class parser():
    def __init__(self, fileName: str):
        self.fileName= fileName
        self.headers= []

    # get includes from each file
    def getHeaders(self):
        rf = open(self.fileName, 'r')
        lines = rf.readlines()
        
        for line in lines:
            if "#include" in line:
                if "dpp" in line:
                    self.headers.append(self.parseHeaders(line))
                

    def parseHeaders(self, item: str):
        # remove spaces and lines
        item= item.replace("\n", "").replace(" ", "")

        # remove comment if present
        if "//" in item:
            item= item[:item.index("//")]

        # remove #include
        item= item.replace("#include", "")

        # remove paranthesis if present
        if "<" in item:
            item= item.replace("<", "").replace(">", "")

        if "dpp" in item:
            item= item.replace("dpp/", "")
        
        return item