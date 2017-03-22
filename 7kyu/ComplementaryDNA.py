def DNA_strand(dna):
    returnString = ""
    dnaMap = {
        "A":"T", 
        "T": "A", 
        "C": "G",
        "G": "C"
        }
    for letter in dna:
        returnString += dnaMap[letter]
    return returnString

# Best
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])