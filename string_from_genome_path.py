#python3
import sys


def reconstruct_string(patterns):
    gen = patterns[0]
    for i in range(1,len(patterns)):
        gen+=patterns[i][-1]
    return gen


if __name__ == "__main__":
    patterns = sys.stdin.read().strip().splitlines()
    '''
    patterns = []
    my = input()
    patterns.append(my)
    while(len(my)>0):
        my = input()
        patterns.append(my)
    patterns.pop(-1)
    '''
    print(reconstruct_string(patterns))
