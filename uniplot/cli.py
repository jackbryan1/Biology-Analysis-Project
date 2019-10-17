import argparse
from . import parse
from . import analysis
from . import plot

LOC="uniprot_receptor.xml.gz"

def dump(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def cli():
    parser = argparse.ArgumentParser(prog="uniplot")

    subparser = parser.add_subparsers(help="Sub Command Help")

    subparser.add_parser("dump").set_defaults(func=dump)
    subparser.add_parser("list").set_defaults(func=names)
    subparser.add_parser("average").set_defaults(func=average)
    subparser.add_parser("plot").set_defaults(func=plot_average_by_taxa)

    args = parser.parse_args()
    args.func(args)

def average(args):
        print("Average Length is {}".format(
            analysis.average_len(parse.uniprot_seqrecords(LOC))))

def plot_average_by_taxa(args):
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)
