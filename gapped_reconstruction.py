#python3
import sys


def reconstruct(k, d, paired_comp):
    """Reconstruct a string from its Paired Composition

    Args:
        k:              the length of the k-mers
        d:              the length of the gap
        paired_comp:    the collection of (k,d)-mers

    Returns:
        a string that has the given paired composition
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    k, d = map(int, sys.stdin.readline().strip().split())
    paired_comp = [line.strip() for line in sys.stdin if line.strip()]

    print(reconstruct(k, d, paired_comp))
