## This approach gest the job done, but there are four iteration over
## the sequence.

fname = 'rosalind_dna.txt'
f = open(fname,'r')
seq = f.read()
f.close()

def count_dna(x):
    dna = x.upper()
    A = str(dna.count('A'))
    C = str(dna.count('C'))
    G = str(dna.count('G'))
    T = str(dna.count('T'))
    return A + ' ' + C + ' ' + G + ' ' + T

output = count_dna(x = seq)

with open('output.txt', 'w') as f:
    f.write(output)

print(output)
