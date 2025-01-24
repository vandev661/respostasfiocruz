def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequences = {}
        sequence_name = ""
        sequence_data = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence_name:
                    sequences[sequence_name] = sequence_data
                sequence_name = line[1:]
                sequence_data = ""
            else:
                sequence_data += line
        if sequence_name:
            sequences[sequence_name] = sequence_data
    return sequences

def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("As sequências devem ter o mesmo comprimento.")
    return sum(1 for base1, base2 in zip(seq1, seq2) if base1 != base2)

sequences = read_fasta('D:/OneDrive/Documentos/1/Atividade 2/alinhamento.fasta')

# Distância entre as sequências A e B
dist_B_A = hamming_distance(sequences['B'], sequences['A'])

# Distância entre as sequências A e C
dist_C_A = hamming_distance(sequences['C'], sequences['A'])

print(f"Distância de Hamming da sequência B em relação a A: {dist_B_A}")
print(f"Distância de Hamming da sequência C em relação a A: {dist_C_A}")
