#!/usr/bin/env python3
from random import random
import argparse

def compute_pi(attempts):
    inside = 0
    tries = 0
    
    # Try the specified number of random points
    while (tries < attempts):
        tries += 1
        if ( (random()**2 + random()**2) < 1):
            inside += 1
    
    # Compute the ratio and return
    result=4*(inside/tries)
    return(result)

if __name__ == '__main__':
    # Use argparse to take command line options and generate help text
    parser = argparse.ArgumentParser()
    parser.add_argument("attempts", help="number of random points (int)", type=int)
    args = parser.parse_args()

    result = compute_pi(args.attempts)
    print( f'Final pi estimate from {args.attempts} attempts = {result}' )

