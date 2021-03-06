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
    parser.add_argument('--filename', help='name of the file')
    parser.add_argument('-depth', type=int, help='depth of the graph')

    subparser = parser.add_subparsers(help="Sub Command Help"
                                           "dump: writes out all data"
                                           "list: lists all names"
                                           "average: calculates average length"
                                           "plot: plots a graph of the average lengths"
                                           "plot_pie: plots a graph of the lengths")

    subparser.add_parser("dump").set_defaults(func=dump, help='writes out all data')
    subparser.add_parser("list").set_defaults(func=names, help='lists all names')
    subparser.add_parser("average").set_defaults(func=average, help='calculates average length')
    subparser.add_parser("plot").set_defaults(func=plot_average_by_taxa, help='plots a graph of the average lengths')
    subparser.add_parser('plot_pie').set_defaults(func=plot_length_by_taxa, help='plots a graph of the lengths')
    args = parser.parse_args()
    print(args)
    args.func(args)

def average(args):
    """Prints the average length of proteins"""
    print("Average Length is {}".format(
         analysis.average_len(parse.uniprot_seqrecords(args.filename))))

def plot_average_by_taxa(args):
    """Plots a graph"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(args.filename), (args.depth))
    plot.plot_bar_show(av)

def plot_length_by_taxa(args):
    length = analysis.len_taxa(parse.uniprot_seqrecords(args.filename), (args.depth))
    plot.plot_pie_show(length)
