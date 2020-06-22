from sys import *
from numpy import *
strand="C"
serial1='-----------'
serial2='---'
rem='CCGAT'
crag=3

def strExt(ss2,serial1):
    ss2[ : 3] + serial1 + ss2[3 : ] 

    return
def strExtr(ss2,serial2):
    ss2[ : 45] + serial2 + ss2[45 : ] 
    return

def reactify(NE, o, p):
    NE-=2
    o+=3
    p-=2