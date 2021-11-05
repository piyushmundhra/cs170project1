import pandas as pd 
from Board import Board

def search():
    ALLNODES = []
    nodes = [Board()]

    while nodes:
        currentnode = nodes[0]
        nodes = nodes[1:]
        if currentnode.isSolved(): return currentnode


    return -1