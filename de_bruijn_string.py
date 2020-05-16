#python3
import sys

def prefix(string):
    return string[:len(string)-1]

def suffix(string):
    return string[1:]

def de_bruijn(k,text):
    """Creates a de Bruijn graph from a string given a value of k

    Args:
        k:          the length of strings represented by edges in the
                    de Bruijn graph
        text:       the string from which the de Bruijn grpah will be
                    constructed

    Returns:
        a string containing an adjacency list representation of the de Bruijn
        graph as described in the problem specification
    """
    # TODO: your code here
    d = {}
    for i in range(len(text)-k+1):
        if text[i:k+i-1] not in d.keys():
            d[text[i:k+i-1]] = [text[i+1:k+i]]
        else:
            d[text[i:k+i-1]].append(text[i+1:k+i])
    for i in d:
        res = i+" -> "
        for j in d[i]:
            res+=j+","
        print(res[:-1])
    


if __name__ == "__main__":
    k = int(input().strip())
    text = input().strip()
    de_bruijn(k,text)
