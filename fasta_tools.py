from Bio import SeqIO

def analyze_fasta(file_path):
    for record in SeqIO.parse(file_path, "fasta"):
        seq = record.seq.upper()
        length = len(seq)
        gc_count = seq.count("G") + seq.count("C")
        gc_percent = (gc_count / length) * 100 if length > 0 else 0
        print(f"{record.id}: Length={length}, GC%={gc_percent:.2f}")

if __name__ == "__main__":
    fasta_file = "example.fasta"  # Change if needed
    analyze_fasta(fasta_file)
