#python3
import sys

def string_spelled_by_g_p(gappedPatterns, kVal, dVal):
    firstPatterns = []
    secondPatterns = []
    for kDmers in gappedPatterns:
        firstPatterns.append(kDmers[0])
        secondPatterns.append(kDmers[1])
    deBruijnGP = paired_kmer_debruijn(gappedPatterns)
    eulerianPathRP = construct_eulerian_path(deBruijnGP)
    fPatterns = []
    sPatterns = []
    for step in eulerianPathRP:
        fPatterns.append(step.split('|')[0])
        sPatterns.append(step.split('|')[1])
    prefixString = reconstruct_string(fPatterns)
    suffixString = reconstruct_string(sPatterns)
    prefixEnder = kVal + dVal + 1
    for i in range(prefixEnder, len(prefixString) + 1):
        suffixOverlap = i - kVal - dVal
        if prefixString[i] != suffixString[suffixOverlap]:
            return 'There is no string spelled by the gapped patterns'
        return prefixString + suffixString[-(prefixEnder - 1):]
    
def construct_eulerian_path(gMap):
    cycle = []
    gMapKeys = list(gMap.keys())
    for listKey in gMapKeys:
        incomingEdges = 0
        outgoingEdges = gMap[listKey]
        if outgoingEdges not in gMap:
            unbalancedNode = outgoingEdges
            unbalancedInOutNode = unbalancedNode
            gMap[unbalancedNode] = []
        for dictionaryKey in gMap:
            edges = gMap[dictionaryKey]
            if listKey == edges:
                incomingEdges += 1
        outgoingEdges = outgoingEdges.count('|')
        outMinusIn = outgoingEdges - incomingEdges
        inMinusOut = incomingEdges - outgoingEdges
        if outMinusIn == 1:
            unbalancedOutInNode = listKey
            activeNode = listKey
            cycle.append(activeNode)
        elif inMinusOut == 1:
            unbalancedInOutNode = listKey
            unbalancedNode = listKey
    gMap[unbalancedInOutNode] = unbalancedOutInNode
    eulerianCycle = construct_ec_from_pr(gMap)
    for i in range(len(eulerianCycle)-1):
        if i == len(eulerianCycle):
            break
        if eulerianCycle[i] == unbalancedInOutNode and eulerianCycle[i+1] == unbalancedOutInNode:
            eulerianPath = eulerianCycle[i+1:] + eulerianCycle[1:i+1]
            return eulerianPath

def construct_ec_from_pr(gMap):
    node = next(iter(gMap))
    cycle = []
    cycle.append(node)
    while len(gMap) > 0:
        if node in gMap:
            step = gMap[node]
            cycle.append(step)
            del gMap[node]
            node = step
        else:
            for i in range(len(cycle) - 1):
                startPoint = cycle[i]
                if startPoint in gMap:
                    cutOffPoint = i
                    node = startPoint
            lastEdge = cycle[len(cycle) - 1]
            newCycle = []
            for edge in cycle[cutOffPoint:]:
                newCycle.append(edge)
            for moreEdge in cycle[1:cutOffPoint + 1]:
                newCycle.append(moreEdge)
            cycle = newCycle
    return cycle

def reconstruct_string(kmers):
    reconstructedString = ''
    reconstructedString += kmers[0]
    for i in range(len(kmers) - 1):
        if kmers[i][-(len(kmers[0]) - 1):] == kmers[i+1][:(len(kmers[0]) - 1)]:
            reconstructedString += kmers[i+1][-1:]
    return reconstructedString

def paired_kmer_debruijn(pairedKmers):
    graphMap = {}
    prefixPRList = []
    suffixPRList = []
    for pairedKmer in pairedKmers:
        prefixPR = ''
        suffixPR = ''
        for i in range (len(pairedKmer)):
            prefixPR += (_prefix(pairedKmer[i]))
            suffixPR += (_suffix(pairedKmer[i]))
            if i == 0:
                prefixPR += '|'
                suffixPR += '|'
        graphMap[prefixPR] = suffixPR
    return graphMap
# ----------------------------------------------------------------------
def _prefix(text):
    return text[:len(text)-1]
# ----------------------------------------------------------------------
def _suffix(text):
    return text[-(len(text) - 1):]
# ---MAINCODE-----------------------------------------------------------
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count


if __name__ == "__main__":
    kVal, dVal = map(int, sys.stdin.readline().strip().split())
    rawData = [line.strip() for line in sys.stdin if line.strip()]    
    
    gappedPatterns = []
    for line in rawData:
        gappedPattern = line.split("|")
        gappedPatterns.append(gappedPattern)
    
    myAnswer = string_spelled_by_g_p(gappedPatterns, kVal, dVal)
    print(myAnswer)