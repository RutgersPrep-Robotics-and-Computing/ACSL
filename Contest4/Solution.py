#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'numFibonacciCycles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. FLOAT realPartLL
#  2. FLOAT imagPartLL
#  3. FLOAT realPartUR
#  4. FLOAT imagPartUR
#  5. FLOAT incr
#

def absValue(Real, Imaginary) -> float:
    return math.sqrt(Real * Real + Imaginary * Imaginary)

def add(Real1, Imaginary1, Real2, Imaginary2):
    return (Real1 + Real2, Imaginary1 + Imaginary2)

def multiply(Real1, Imaginary1, Real2, Imaginary2):
    pass

def numFibonacciCycles(realPartLL, imagPartLL, realPartUR, imagPartUR, incr) -> int:
    
    print(realPartLL, imagPartLL, realPartUR, imagPartUR, incr)

    pass

if __name__ == '__main__':
    realPartLL, imagPartLL, realPartUR, imagPartUR, incr = [float(x) for x in open("input.in", "r").readlines()]

    numFibonacciCycles(realPartLL, imagPartLL, realPartUR, imagPartUR, incr)