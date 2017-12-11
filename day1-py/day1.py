""" Day 1 solution """
import sys
import os.path

def finddupes(number):
    """Finds duplicate numbers circularly"""
    dupes = []
    for (i, x) in enumerate(number):
        try:
            if x == number[i+1]:
                dupes.append(int(x))
        except:
            if x == number[0]:
                dupes.append(int(x))
    return dupes

# main
CAPTCHA = sys.argv[1]
NUMS = []
if os.path.isfile(CAPTCHA):
    with open(CAPTCHA, 'r') as f:
        INPUT = f.read()
    NUMS = finddupes(INPUT)
else:
    NUMS = finddupes(CAPTCHA)

print('{}'.format(sum(NUMS)))
