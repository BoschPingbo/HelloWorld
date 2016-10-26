# pi.py
"""from random import random
from math import sqrt
from time import clock"""
import random
import math
import time
import random
import pdb

DARTS = 1200
hits = 0
time.clock()
for i in range(1,DARTS):
    x, y = random.random(), random.random()
    dist =  math.sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("Pi的值是 %s" % pi)
print("程序运行时间是 %-5.5ss" % time.clock())
