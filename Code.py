from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import matplotlib.pyplot as plt

# Set parameters for the genome sequences

# Define your own sequences

# by typing

# seq1 = "ATAGATAGACAGATAGGATAGATAGAGAGAGATATATTATATGATAGATTGATAGGATGATAGTATTTAGCAGAT"
# seq2 = "CAGATAGACTAGATATATACTACTACTACGACAGCAGCAGCAGACGACGACGACTATACATCATAGATAGATATATACAGATATAGACAGATGAT"


# by reading

with open('seq1.txt', 'r') as file:
    seq1 = file.read()

with open('seq2.txt', 'r') as file:
    seq2 = file.read()

print(seq1)
print(seq2)
print(len(seq1))
print(len(seq2))
genome_length = min(len(seq1), len(seq2))
# Convert the sequence strings to Seq objects
seq1 = Seq(seq1)
seq2 = Seq(seq2)

# Calculate the similarity between the two sequences
matches = 0
for i in range(genome_length):
    if seq1[i] == seq2[i]:
        matches += 1

similarity = matches / genome_length

# Print the similarity between the two sequences
print(f"Similarity: {similarity}")

# Write the genome sequences to FASTA files
SeqIO.write(SeqRecord(seq1, id="sequence1", description=""), "sequence1.fasta", "fasta")
SeqIO.write(SeqRecord(seq2, id="sequence2", description=""), "sequence2.fasta", "fasta")

# Generate a dot plot to visualize the similarity between the sequences
fig, ax = plt.subplots()
ax.matshow([[int(seq1[i] == seq2[j]) for j in range(genome_length)] for i in range(genome_length)])
ax.set_title("Sequence similarity")
ax.set_xlabel("Sequence 2")
ax.set_ylabel("Sequence 1")
plt.show()







