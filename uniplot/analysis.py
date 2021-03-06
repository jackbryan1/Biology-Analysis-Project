def average_len(records):
        """Returns the average len for records"""
        RecordLength = [len(i) for i in records]
        return sum(RecordLength) / len(RecordLength)

def average_len_taxa(records, depth):
    """Returns the average length for the top level taxa"""
    if depth is None:
        depth = int(0)
    record_by_taxa = {}
    for r in records:
        try:
            taxa = r.annotations["taxonomy"][depth]
        except:
            print()
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}

def len_taxa(records, depth):
    """Returns the average length for the top level taxa"""
    if depth is None:
        depth = int(0)
    record_by_taxa = {}
    for r in records:
        try:
            taxa = r.annotations["taxonomy"][depth]
        except:
            print()
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:len(record) for (taxa, record) in record_by_taxa.items()}
