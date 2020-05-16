#python3
import sys
import collections

def prefix(string):
    return string[:len(string)-1]

def suffix(string):
    return string[1:]

def overlap_graph(patterns):
    """Creates an overlap graph from a list of k-mers

    Args:
        patterns:       a list of string k-mers

    Returns:
        a string containing an adjacency list representation of the overlap
        graph as described in the problem specification
    """
    # TODO: your code here
    patterns = list(set(patterns))
    pat_len = len(patterns)
    #pairs = []
    for i in range(pat_len):
        res = str(patterns[i]) + " -> "
        flag = 0
        for j in range(pat_len):
            if(suffix(patterns[i]) == prefix(patterns[j])):
                res += str(patterns[j])+","
                flag = 1
        if(flag==1):
            print(res[:-1])


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
    overlap_graph(patterns)
