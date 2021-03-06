
from __future__ import generators

file = open("listing20-1.txt","r")
def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
    

if __name__=="__main__":
    blocks(file)
