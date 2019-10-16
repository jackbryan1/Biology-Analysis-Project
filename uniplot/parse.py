import gzip
from Bio import SeqIO

def uniprot_seqrecords(file_location):
        records = []

        handle = gzip.open("uniprot_receptor.xml.gz")
        for record in SeqIO.parse(handle, "uniprot-xml"):
            records.append(record)

        return records
