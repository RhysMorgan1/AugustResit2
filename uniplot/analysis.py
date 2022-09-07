def average_len(records):
    """"Return average record length"""
    count = 0
    NumberOfRecords = 0
    Average = 0
    for record in records:
        count = count + len(record)
        NumberOfRecords += 1
    Average = count/NumberOfRecords
    return round(Average)

def average_len_taxa(records, depth):
    """"Return count of records and and teh average for the records"""
    CountOfRecords = {}
    TaxaRecord = {}    
    RecordName = []
    depth = int(depth)
    if depth <= 0:
        depth = 0
    elif depth > 0:
        depth = depth - 1
    for record in records:
        taxa = record.annotations["taxonomy"][depth]
        if taxa in TaxaRecord:
            CountOfRecords[taxa] = CountOfRecords[taxa] + 1
            TaxaRecord[taxa][0] = TaxaRecord[taxa][0]+1
            TaxaRecord[taxa][1] = TaxaRecord[taxa][1] + len(record)
        else:
            TaxaRecord.setdefault(taxa, [1, len(record)])
            CountOfRecords.setdefault(taxa, 1)
            RecordName.append(taxa)
    for i in RecordName:
        TaxaRecord[i][1] = TaxaRecord[i][1]/CountOfRecords[i]
    return TaxaRecord




