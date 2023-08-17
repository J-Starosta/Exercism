RNA = ['C', 'G', 'A', 'U']
DNA = ['G', 'C', 'T', 'A']

def to_rna(dna_strand):
    result = []
    for element in dna_strand:
        result.append(RNA[DNA.index(element)])
    return ''.join(result)
