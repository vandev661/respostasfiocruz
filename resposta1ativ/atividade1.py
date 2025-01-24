
import os

os.chdir('D:/OneDrive/Documentos/1/Atividade 1') 

#Item A)
def count_nucleotides(dna_content):
	return {
		'A': dna_content.count('A'),
		'T': dna_content.count('T'),
		'C': dna_content.count('C'),
		'G': dna_content.count('G')
}

#Item B)
def transcribe_dna_to_rna(dna_content):
	complementary_dna = dna_content.replace('A', 'X').replace('T', 'A').replace('X', 'T')
	complementary_dna = complementary_dna.replace('C', 'Y').replace('G', 'C').replace('Y', 'G')

	return complementary_dna.replace('T', 'U')	
		

#Item C)
cdna_table = {
	'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
	'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
	'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
	'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
	'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
	'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
	'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
	'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
	'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
	'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
	'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
	'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
	'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
	'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
	'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
	'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'	
}	

def process_dna():
	with open('dna.txt', 'r') as dna_file:
		dna_content = dna_file.read()

	nucleotide_counts = count_nucleotides(dna_content)
	#Resposta Item A)
	print(nucleotide_counts)

	rna_content = transcribe_dna_to_rna(dna_content)
	with open('rna.txt', 'w') as rna_file:
		#Resposta Item B)
		rna_file.write(rna_content)

	with open('rna.txt', 'r') as rna_file:
		rna_content = rna_file.read()

	aa_content = ''
	for i in range(0, len(rna_content), 3):
		aa_content += cdna_table.get(rna_content[i:i+3], '') + ' '

	with open('aa.txt', 'w') as aa_file:
		#Resposta Item C)
		aa_file.write(aa_content)

process_dna()
