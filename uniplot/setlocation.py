def setlocation(input):
    """Write the desired file location"""
    MyFile = open("./uniplot/dataloc", "w")
    MyFile.write(input)
    MyFile.close()

def readlocation():
    """Reading the location from teh file"""
    MyFile = open("./uniplot/location", "r")
    location = MyFile.read()
    location = location.strip()
    return location