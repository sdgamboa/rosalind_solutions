## This code is more verbose, but it should be faster.
## There is only one interation over each of the bases.

with open('rosalind_dna.txt', 'r') as f:
    seq = f.read()

def count_dna(x):
    dna = x.upper()
    A = 0
    C = 0
    G = 0
    T = 0
    for i in dna:
        if i == 'A':
            A = A + 1
        if i == 'C':
            C = C + 1
        if i == 'G':
            G = G + 1
        if i == 'T':
            T = T + 1
    output = str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T)
    return output

res = count_dna(x = seq)
print(res)
