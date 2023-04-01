# Biocomputing coursework project notebook.
# In this notebook, all the code that will be submitted to GitHub and Gradescope
# will be tried out and optimized as much as possible before deadline.

# trying with biopython
import argparse
from Bio import SeqIO
# function for obtaining match
# scores
def seq_al(target, database):
    # importing libraries
    import decimal
    from Bio import Align
    # specifying each match
    # adds 1.0 to the score
    aligner = Align.PairwiseAligner(match_score=1.0)
    # getting score from target
    # versus database sequence
    score = aligner.score(target.seq, database.seq)
    # calculating score percentage
    dec_score = (score/len(database.seq))*100
    # making result to be only
    # two values after decimal
    result = decimal.Decimal(dec_score).quantize(decimal.Decimal('0.00'))
    #converting result to float
    # for better manipulation
    return float(result)
# creating final function to
# obtain most probable breed
def get_breed(target, dogs_seqs):
    # creating empty list for
    # every alignment score
    every_score = []
    # iterating over database sequences
    for i in dogs_seqs:
        # running scoring function
        # for each sequence in database
        # vs target sequence
        every_score.append(seq_al(target, i))
    # getting index of highest score
    # to call this obtained index
    # in the breeds list
    top_breed = every_score.index(max(every_score))
    return f"This sample has a higher chance of being a{breed[top_breed].replace('[','').replace('breed=','')}, with a percentage of {max(every_score)}% and a 100% chance of being a good boy"
if __name__=='__main__':
    # read database fasta file
    database_file = './dog_breeds.fa'
    # parsing sequences with seqio as
    # fasta format
    seqs = list(SeqIO.parse(database_file, 'fasta'))
    # creating list for getting breeds
    breed = []
    # getting each seqrecord from
    # database
    for seq in seqs:
        # spliting descriptions to
        # separate [breed]
        desc = seq.description.split(']')
        # iterating through descriptions
        for i in desc:
            # separating the breeds
            # and adding them to list
            if 'breed' in i and '=' in i:
                breed.append(i)
    # creating arguments
    parser = argparse.ArgumentParser(prog='BreedDetector', description=f"Detects the breed of your dog through its DNA sequence using {database_file} as database.")
    # input
    parser.add_argument('-f', '--file', help='Fasta file of your dog')
    # output
    parser.add_argument('-o', '--output', help='Name of the results file')
    args = parser.parse_args()
    # reading my target sequence as fasta
    sample = SeqIO.read(args.file, 'fasta')
    # calling alignment
    my_breed = get_breed(sample, seqs)
    with open(args.output, 'w') as f:
        f.write(my_breed)