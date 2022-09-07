
def SaveLocation(var):
    """Save inputted file location"""
    MyFile = open('./uniplot/dataloc', 'w')
    MyFile.write(var)
    MyFile.close()

def ReadLocation():
    """Read the saved location from specified file"""
    MyFile = open('./uniplot/dataloc', 'r')
    location = MyFile.read()
    return location.strip()
