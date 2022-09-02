import matplotlib.pyplot as plt

def plot_bar_show(d, chartType):
    """Shows average length of taxonomy in a bar or pie chart"""
    Average = [i[1] for i in list(d.values())]

    if chartType == 1:
        plt.pie(Average, labels=d.keys())
        plt.show

    else:
        range = range(0, len(d))
        plt.figure()
        plt.bar(range, Average)
        plt.xticks(range, d.keys())
        plt.xticks(rotation=90)
        plt.show()

def plot_pie_show(d):
    NumofRecords = [i[0] for i in list(d.values())]
    y = [i + "\n" + str(j[0]) for i, j in d.items()]
    plt.pie(NumofRecords, labels=y)
    plt.show()
