import argparse
import gzip
from Bio import SeqIO

def dump(args):
    handle = gzip.open("uniprot_receptor.xml.gz")
    for record in SeqIO.parse(handle, "uniprot-xml"):
        print(record)

def names(args):
    handle = gzip.open("uniprot_receptor.xml.gz")
    for record in SeqIO.parse(handle, "uniprot-xml"):
        print(record.name)

def cli():
    parser = argparse.ArgumentParser(prog="uniplot")

    subparser = parser.add_subparsers(help="Sub Command Help")

    subparser.add_parser("dump").set_defaults(func=dump)
    subparser.add_parser("list").set_defaults(func=names)

    args = parser.parse_args()
    args.func(args)
