from sys import *
from numpy import *

class sequence:
    seq1 = 'ACATGCTACACGTATCCGATACCCCGTAACCGATAACGATACACAGACCTCGTACGCTTGCTACAACGTACTCTATAACCGAGAACGATTGACATGCCTCGTACACATGCTACACGTACTCCGAT'
    seq2 = 'ACATGCGACACTACTCCGATACCCCGTAACCGATAACGATACAGAGACCTCGTACGCTTGCTAATAACCGAGAACGATTGACATTCCTCGTACAGCTACACGTACTCCGAT'
    rows = len(seq1)+1
    cols = len(seq2)+1
    try:
        # use fast numerical arrays if we can
        a = zeros((rows, cols), float)
    except ImportError:
        # use a list if we have to
        a = []
        for i in range(rows):
            a += [[0.]*cols]
