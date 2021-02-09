from Bio import AlignIO
from glob import glob
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Nexus import Nexus


def convert_fasta_to_nexus(input: str, output: str):
    AlignIO.convert(input, "fasta", output, "nexus", "DNA")
    print(f"{input} has been sucessfully converted to {output}.fasta")

def concat_nexus_alignment(path: str, output_name: str):
    wildcards = path + "/*.nex"
    outname = path + "/" + output_name
    fnames = glob(wildcards)
    nex_list = [(nex, Nexus.Nexus(nex)) for nex in fnames]

    concat = Nexus.combine(nex_list)
    concat.write_nexus_data(filename=open(outname, "w"))
    print("DONE!")

def get_path(path: str, fname: str) -> str :
    return path + "/" + fname    