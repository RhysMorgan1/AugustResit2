

def average_len(records):
    i = 0
    NumRecord = 0
    Average = 0
    for record in records:
        i += len(record)
        NumRecord += 1
    Average = i / NumRecord
    return round(Average)


def average_len_taxa(records, DataDepth):
    """Returns the average length for the top level taxa"""
    record_by_taxa = {}
    RecordCount = {}
    RecordNames = {}

    DataDepth = int(DataDepth)
    if DataDepth > 0:
        DataDepth = DataDepth -1
    for record in records:
        taxa = record.annotations["taxonomy"][DataDepth]
        if taxa in record_by_taxa:
            RecordCount[taxa] = RecordCount[taxa] + 1
            record_by_taxa[taxa][0] = record_by_taxa[taxa][0]+1
            record_by_taxa[taxa][1] = record_by_taxa[taxa][1] + len(record)
        else:
            record_by_taxa.setdefault(taxa, [1, len(record)])
            RecordCount.setdefault(taxa, 1)
            RecordNames.append(taxa)
    for i in RecordNames:
        record_by_taxa[i][1] = record_by_taxa[i][1]/RecordCount[i]
    return record_by_taxa



