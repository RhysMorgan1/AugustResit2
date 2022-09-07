from . import parse 
from . import analysis 
from . import plot
from . import setlocation
import argparse



def PieChartFunc(location, args):
    """Plot records as a pie chart"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(location), args.depth)
    plot.display_numpie(av)

def location(UserInput):
    """Save entered file location"""
    setlocation.SaveLocation(UserInput.location)
def FileLocation(args, loco = None):
    """Use teh file locations to run the functions"""
    location = setlocation.ReadLocation()
    if loco != None:
        args.func(loco, args)
    else:
        args.func(location, args)




def dump(location, args):
    """Print all records"""
    for record in parse.uniprot_seqrecords(location):
        print(record)

def names(location, args):
    """Print all record names"""
    for record in parse.uniprot_seqrecords(location):
        print(record.name)

def average(location, args):
    """Print the average length of all proteins to terminal"""
    print("Average Length is {}".format(analysis.average_len(parse.uniprot_seqrecords(location))))

def plot_average_by_taxa(location, args):
    """Displaygraph of proteins by their taxas"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(location), args.depth)
    plot.display_barplot(av, args.piemode)








def cli():
    """Parse all arguments from commandline and call appropriate functions"""
    #Create new parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--location", type=str, default=None, metavar='file-location')
    #Add subparsers
    subparsers = parser.add_subparsers(help="Sub Command Help")

    
    subparsers.add_parser("dump").set_defaults(run=FileLocation, func=dump)
    subparsers.add_parser("list").set_defaults(run=FileLocation, func=names)
    subparsers.add_parser("average").set_defaults(run=FileLocation, func=average)
    LocationOfFile = subparsers.add_parser('location')
    LocationOfFile.add_argument('location', type=str,metavar='file_location')
    LocationOfFile.set_defaults(func=location)
    PieChart = subparsers.add_parser("pie")
    PieChart.add_argument("--depth", type=int, default=0)
    PieChart.set_defaults(run=FileLocation, func=PieChartFunc)
    TaxaPlots = subparsers.add_parser("plot-taxa")
    TaxaPlots.add_argument("--depth", type=int, default=0,metavar="Leven number")
    TaxaPlots.add_argument("--piemode", type=int, default=0,metavar="1/0")
    TaxaPlots.set_defaults(run=FileLocation, func=plot_average_by_taxa)
    

    #Parse the command line
    args = parser.parse_args()
    args.run(args, args.location)

