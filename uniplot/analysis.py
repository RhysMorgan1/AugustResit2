

def average_len(records):
    i = 0
    NumRecord = 0
    Average = 0
    for record in records:
        i += len(record)
        NumRecord += 1
    Average = i / NumRecord
    return round(Average)


def average_len_taxa(records):
    """Returns the average length for the top level taxa"""
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][0]


        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}

