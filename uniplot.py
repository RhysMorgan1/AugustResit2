import gzip
from Bio import SeqIO



#for l in gzip.open("uniprot_receptor.xml.gz"):
#    print(l.decode().strip())



handle=gzip.open("uniprot_receptor.xml.gz")
for record in SeqIO.parse(handle, "uniprot-xml"):
    print(record)