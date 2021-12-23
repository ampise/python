import os
os.system("clear")

# Already identified sequences of irregular DNA’s found in bacteria and viruses of common diseases are as follows:

# Malaria - GBC
# Typhoid - GCD
# HIV - GAA
# SARS - CAC

# TASK:

# Provided a full non-repeating DNA sequence of a patient.
# Identify presence of one or more common diseases in that patient by scanning his/her entire DNA sequence.
# Looking for patterns from the common diseases you have already researched above. 
# Output should include list of all the diseases and occurrence of those diseases identified in the complete DNA structure. 

# Example:
# Patient's DNA Sequence - BGDGBCFBCDDFGGCDCFCGBCBCDF
# Found:
# Malaria = 2
# Typhoid = 1

malaria = ["G", "B", "C"]
typhoid = ["B", "G", "D"]
hiv = ["C", "F", "B"]
sars = ["F", "G", "G"]
dna = []
foundMalaria = 0
foundTyphoid = 0
foundHIV = 0
foundSARS = 0

dnaString = input("Please enter patient's DNA sequence: ").upper()
for i in range(len(dnaString)):
    dna.append(dnaString[i])


# Find positives in DNA matches
def findMatches(diseaseDNA, patientDNA):
    diseaseMatches = 0
    for searchPosition in range(len(patientDNA) - len(diseaseDNA) + 1):
        positives = 0
        for d in range(len(diseaseDNA)):
            if diseaseDNA[d] == patientDNA[searchPosition + d]:
                positives = positives + 1
        if positives == len(diseaseDNA):
            diseaseMatches = diseaseMatches + 1
    return diseaseMatches


print("Malaria (", "-".join(malaria), ") =", findMatches(malaria, dna))
print("Typhoid (", "-".join(typhoid), ") =", findMatches(typhoid, dna))
print("HIV (", "-".join(hiv), ") =" , findMatches(hiv, dna))
print("SARS (", "-".join(sars), ") =" , findMatches(sars, dna))
