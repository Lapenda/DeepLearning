#how to make a one hot encoded vector:

import glob
import numpy as np


text_files = glob.glob('./Gutenberg/txt/*.txt')
print("Files: ", text_files)

first_10_files = text_files[:10]

print("\n\nFirst 10 files: ", first_10_files)

svi = []

for file in first_10_files:
    with open (file, 'r') as f:
        temp = f.read()
        svi.append(temp)
        
svi = ''.join(svi)

print("Sav tekst: ", svi)

lista_karaktera = [char for char in svi]
print("\n\nLista karaktera: ", lista_karaktera)
print("\n\nBroj karaktera iz liste: ", len(lista_karaktera))


set_karaktera = set(lista_karaktera)
print("\n\nSet karaktera: ", set_karaktera)
print("\nBroj karaktera: ", len(set_karaktera))

char_index = dict((c, i) for i, c in enumerate(set_karaktera))
index_char = dict((i, c) for i, c in enumerate(set_karaktera))


for char in lista_karaktera[:1000]:
    print(char_index[char], end=' ')
print()


for char in lista_karaktera[:1000]:
    print(index_char[char_index[char]], end='')
print()


sequences = []
maxlen = 50
step = 5

for i in range(0, len(lista_karaktera) - maxlen, step):
    sequences.append(lista_karaktera[i:i + maxlen])
print("\nNumber of sequences: ", len(sequences))


print("Vectorizing...")

network_input = np.zeros((len(sequences), maxlen, len(set_karaktera)), dtype=np.bool)
for i, sequence in enumerate(sequences):
    for t, char in enumerate(sequence):
        network_input[i, t, char_index[char]] = 1
    if i % 10000 == 0:
        print(f"Vectorized {i} of {len(sequences)}")