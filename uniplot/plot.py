import matplotlib.pyplot as mlot

def display_barplot (d, type):
    """Show average length of taxa on a pie or bar chart"""
    AverageLength = [i[1] for i in list(d.values())]
    if type == 1:
        mlot.pie(AverageLength, labels=d.keys())
        mlot.show()
    else:
        Range = range(0, len(d))
        mlot.figure()
        mlot.bar(Range, AverageLength)
        mlot.xticks(Range, d.keys())      
        mlot.subplots_adjust(bottom=0.3)
        mlot.show()

def display_numpie (d):
    """Show pie chart via taxa category"""
    NumberOfRecords = [i[0] for i in list(d.values())]
    y = [i + '\n' + str(j[0]) for i, j in d.items()]
    mlot.pie(NumberOfRecords, labels=y)
    mlot.show()
