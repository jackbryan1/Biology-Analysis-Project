import argparse
from . import parse

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

    args = parser.parse_args()
    args.func(args)
