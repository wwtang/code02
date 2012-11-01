import re
import sys

def try_findall(filename):
    f = open(filename, "r")
    text = f.read()

    tuples = re.findall(r"(\w+) (\w+)", text)

    return tuples
