""" Day 1 solution """
import sys
import os.path

def finddupes(number, offset):
    """Finds duplicate numbers by matching current idx with an offset"""
    end = len(number)
    dupes = []
    for (idx1, val) in enumerate(number):
        nval = int(val)
        idx2 = (idx1 + offset) % end
        if nval == int(number[idx2]):
            dupes.append(nval)
    return dupes

# main
CAPTCHA = sys.argv[1]
OFFSET = len(sys.argv) > 2 and sys.argv[2] or None 
NUMS = []
if os.path.isfile(CAPTCHA):
    with open(CAPTCHA, 'r') as f:
        INPUT = f.read()
    NUMS = finddupes(INPUT, OFFSET and int(OFFSET) or int(len(INPUT)/2))
else:
    NUMS = finddupes(CAPTCHA, OFFSET and int(OFFSET) or int(len(CAPTCHA)/2))

print('{}'.format(sum(NUMS)))
