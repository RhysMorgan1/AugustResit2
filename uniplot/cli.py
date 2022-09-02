import argparse
from . import parse
from . import analysis
from . import plot
from . import setlocation





def FileLoc(input):
    """Saving the wanted file location"""
    setlocation.setlocation(input.location)

def plot_average_by_taxa(Fileloc, args):
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(Fileloc))
    plot.plot_bar_show(av)




def average(Fileloc, args):
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(Fileloc))))


def dump(Fileloc, args):
    for record in parse.uniprot_seqrecords(Fileloc):
        print(record)

def names(Fileloc, args):
    for record in parse.uniprot_seqrecords(Fileloc):
        print(record.name)

def cli():
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    ## Add subparsers
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("plot-average-by-taxa").set_defaults(func=plot_average_by_taxa)

    File_Location = subparsers.add_parser("location").add_argument("location", type=str, metavar="file_location").set_defaults(func=FileLoc)
    ## Parse the command line
    args = parser.parse_args()

    ## Take the func argument, which points to our function and call it.
    args.func(args)


