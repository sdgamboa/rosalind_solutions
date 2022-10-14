import sys

try:
    sys.argv[1]
except IndexError:
    exit('You need to specify a filename')
else:
    fname = sys.argv[1]

with  open(fname, 'r') as f:
    seq = f.read()

def dna_to_rna(x):
    dna = x.upper()
    rna = ''
    for i in dna:
       if i == 'T':
           rna = rna + 'U'
       else:
           rna = rna + i
    return rna

output = dna_to_rna(x = seq)

with open('output.txt', 'w') as f:
    f.write(output)

print('This is the answer:')
print(output)
print('Printing to "output.txt"')
