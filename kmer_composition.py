#python3
import sys

def kmer_composition(k, text):
    """Computes the k-mer composition of string text

    Args:
        k:          integer length of k-mers to be found
        text:       string to split into a k-mer composition

    Returns:
        a string with each k-mer in text separated by newlines
    """
    # TODO: your code here
    d = {}
    for i in range(len(text)-k+1):
        print(text[i:k+i])
    '''        
        if(text[i:k+i] in d.keys()):
            d[text[i:k+i]] += 1
        else:
            d[text[i:k+i]] = 1
    print(d)
    '''


if __name__ == "__main__":
    k = int(input())
    text = input()

    kmer_composition(k, text)
