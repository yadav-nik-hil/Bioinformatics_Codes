#python3
import sys

def de_bruijn(patterns):
    # TODO: your code here
    d = {}
    for text in patterns:
        if text[:-1] not in d.keys():
            d[text[:-1]] = [text[1:]]
        else:
            d[text[:-1]].append(text[1:])
    for i in d:
        res = i+" -> "
        for j in d[i]:
            res+=j+","
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
    de_bruijn(patterns)
