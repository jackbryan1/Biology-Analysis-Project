import argparse
from . import parse
from . import analysis
from . import plot

def dump(args):
    """Prints all records"""
    for record in parse.uniprot_seqrecords(args.filename):
        print(record)

def names(args):
    """Prints all names"""
    for record in parse.uniprot_seqrecords(args.filename):
        print(record.name)

def cli():
    """Deals with parsing"""
    parser = argparse.ArgumentParser(prog="uniplot")
    parser.add_argument('--filename')
    parser.add_argument('-depth', type=int)

    subparser = parser.add_subparsers(help="Sub Command Help")

    subparser.add_parser("dump").set_defaults(func=dump)
    subparser.add_parser("list").set_defaults(func=names)
    subparser.add_parser("average").set_defaults(func=average)
    subparser.add_parser("plot").set_defaults(func=plot_average_by_taxa)

    args = parser.parse_args()
    print(args)
    args.func(args)

def average(args):
    """Prints the average length of proteins"""
    print("Average Length is {}".format(
         analysis.average_len(parse.uniprot_seqrecords(args.filename))))

def plot_average_by_taxa(args):
    """Plots a graph of the average length of proteins in each taxa"""
    if args.depth is not None:
        args.depth = args.depth - 1
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(args.filename), (args.depth))
    plot.plot_bar_show(av)
