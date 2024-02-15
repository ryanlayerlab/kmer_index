# kmer_index
Using k-mers to search strings


## Smith-Waterman
### Usage
```
usage: sw.py [-h] --A A --B B [--gap GAP] [--miss MISS] [--match MATCH]

optional arguments:
  -h, --help     show this help message and exit
  --A A          Sequence A
  --B B          Sequence B
  --gap GAP      Gap penalty (default: -2)
  --miss MISS    Mismatch penalty (default: -1)
  --match MATCH  Match score (default: 1)
```
### Example
```
$ python sw.py --A ACTGGTCA --B CGTGGACA
4
TGGTCA
||| ||
TGGACA
```
