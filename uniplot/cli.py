import argparse
from . import parse
from . import analysis

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

    args = parser.parse_args()
    args.func(args)

def average(args):
        print("Average Length is {}".format(
            analysis.average_len(parse.uniprot_seqrecords(LOC))))
