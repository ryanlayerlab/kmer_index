import argparse
import utils
import numpy as np
import sw

def get_args():
    parser = argparse.ArgumentParser(description='Kmer index')
    parser.add_argument('-k',
                        '--kmer',
                        help='Kmer size',
                        type=int, default=3)

    parser.add_argument('--reference',
                        help='Reference sequence file',
                        type=str,
                        required=True)

    parser.add_argument('--read_size',
                        help='Read size (default: 100)',
                        type=int,
                        default=100)

    parser.add_argument('--num_reads',
                        help='Number of reads',
                        type=int,
                        required=True)

    parser.add_argument('--error_rate',
                        help='Error rate',
                        type=float,
                        default=0.01)

    parser.add_argument('--max_mismatches',
                        help='Maximum number of mismatches',
                        type=int,
                        default=3)

    return parser.parse_args()

def get_kmer_index(T, k):
    return None

def align_read():
    ################################################################################
    # YOUR CODE HERE
    ################################################################################
    alignments = []

    for hit in hits:
        hit_seq = T[hit:hit+len(read)]
        score, align_A, align_B, match = sw.sw(hit_seq, read, gap, miss, match)

    return alignments

def align_reads():
    return None

def main():
    args = get_args()
    reference = utils.read_fasta(args.reference)
    T = reference[0][1]

    kmer_index = get_kmer_index(T, args.kmer)

    reads = utils.sim_reads(T,
                            args.read_size,
                            args.num_reads,
                            args.error_rate)

    alignments = align_reads(reads, T, kmer_index, args.max_mismatches)

    for i, read in enumerate(reads):
        for alignment in alignments[i]:
            # Print the read and the alignment

if __name__ == '__main__':
    main()
