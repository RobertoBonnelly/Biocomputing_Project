This program was done with the intention of introducing any dog DNA sequence, compare it to our database sequences, and identifying what breed it is most likely for your dog to be.


Dependencies:
- First of all, you need to download the dog_breeds.fa and the Dogs_Breeds.py files, as these correspond to the database and script respectively.
- As the script is a python file, you will need to have python 3+ installed, as well as the biopython library. You can install these going to www.python.org/downloads/ and when you are finished installing python, you will be able to simply go into your command line and type "pip install biopython".

Usage:
python\python3 ./Dogs_Breeds.py -f input_file in fasta format -o output_directory.

When running this in your command line, the script will take your fasta input file and align it against each sequence in the database dog_breeds.fa, calculating a match percent and storing it in a list, from which the maximum value will be returned with its corresponding breed as the most likely result in the directory specified in the second argument.

A "mystery" fasta file with its result is added in the repository for you to test the program and compare the result you get is correct.

Note: It is important to move(cd) to the directory containing these files before executing.