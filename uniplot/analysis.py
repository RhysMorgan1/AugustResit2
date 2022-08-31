from . import parse
LOC="uniprot_receptor.xml.gz"

def average_len(records):
    i = 0
    NumRecord = 0
    Average = 0
    for record in parse.uniprot_seqrecords(LOC):
        i += len(record)
        NumRecord += 1
    Average = i / NumRecord
    return Average
