import gzip
from Bio import SeqIO
import io

def uniprot_seqrecords(FileLocation):
    handle = gzip.open(FileLocation)
    buff = io.BufferedReader(handle,200000000)
    return SeqIO.parse(buff, "uniprot-xml")
