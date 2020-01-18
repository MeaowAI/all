class ManageFile:
    def readText(self,Readtext,mode):
        File = open(Readtext,mode)
        return File.read()

    def writeText(self,Writetext,mode,text):
        File = open(Writetext,mode)
        File.write(text)
        File.close()
