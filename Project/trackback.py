from sys import *
from numpy import *
import sequence 
class matchSeq:
    obj=sequence.sequence()
    col=obj.cols
    match = 2.
    mismatch = -2.
    gap = -2.   
    s = {
        'AA': match, 'AG': mismatch, 'AC': mismatch, 'AT': mismatch,
        'GA': mismatch, 'GG':     match, 'GC': mismatch, 'GT': mismatch,
        'CA': mismatch, 'CG': mismatch, 'CC':     match, 'CT': mismatch,
        'TA': mismatch, 'TG': mismatch, 'TC': mismatch, 'TT':     match,
    }
    for i in range(obj.rows):
        obj.a[i][0] = 0
    for j in range(obj.cols):
        obj.a[0][j] = 0
    for i in range(1, obj.rows):
        for j in range(1, obj.cols):
            choice1 = obj.a[i-1][j-1] + s[(obj.seq1[i-1] + obj.seq2[j-1])]
            choice2 = obj.a[i-1][j] + gap
            choice3 = obj.a[i][j-1] + gap
            obj.a[i][j] = max(choice1, choice2, choice3)
    aseq1 = ''
    aseq2 = ''
    # We reconstruct the alignment into aseq1 and aseq2,
    i = len(obj.seq1)
    j = len(obj.seq2)
    while i > 0 and j > 0:
        if i % 10 == 0:
            stderr.write('.')

        # by preforming a traceback of how the matrix was filled out above,
        # i.e. we find a shortest path from a[n,m] to a[0,0]
        score = obj.a[i][j]
        score_diag = obj.a[i-1][j-1]
        score_up = obj.a[i][j-1]
        score_left = obj.a[i-1][j]
        if score == score_diag + s[obj.seq1[i-1] + obj.seq2[j-1]]:
            aseq1 = obj.seq1[i-1] + aseq1
            aseq2 = obj.seq2[j-1] + aseq2
            i -= 1
            j -= 1
        elif score == score_left + gap:
            aseq1 = obj.seq1[i-1] + aseq1
            aseq2 = '_' + aseq2
            i -= 1
        elif score == score_up + gap:
            aseq1 = '_' + aseq1
            aseq2 = obj.seq2[j-1] + aseq2
            j -= 1
        else:
            # should never get here..
            print ('ERROR')
            i = 0
            j = 0
            aseq1 = 'ERROR'
            aseq2 = 'ERROR'
            obj.seq1 = 'ERROR'
            obj.seq2 = 'ERROR'
    while i > 0:
        # If we hit j==0 before i==0 we keep going in i.
        aseq1 = obj.seq1[i-1] + aseq1
        aseq2 = '_' + aseq2
        i -= 1

    while j > 0:
        # If we hit i==0 before i==0 we keep going in j.
        aseq1 = '_' + aseq1
        aseq2 = obj.seq2[j-1] + aseq2
        j -= 1

