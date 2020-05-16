#python3
'''
import sys
import re
import heapq
import random
import numpy as np
from itertools import *
from collections import Counter,defaultdict

def de_bruijn(patterns):
    d = {}
    result = []
    for text in patterns:
        if text[:-1] not in d.keys():
            d[text[:-1]] = [text[1:]]
        else:
            d[text[:-1]].append(text[1:])
    for i in d:
        res = i+" -> "
        for j in d[i]:
            res+=j+","
        result.append(res[:-1])
    return result

def construct_eulerian_path(gMap):
# Find Chooses a beginning node by finding the node that has more outgoing edges
# than incoming edges. Als
    cycle = []
    gMapKeys = list(gMap.keys())
    for listKey in gMapKeys:
        incomingEdges = 0
        outgoingEdges = gMap[listKey]
        for outgoingEdge in outgoingEdges:
            if outgoingEdge not in gMap:
                unbalancedNode = outgoingEdge
                unbalancedInOutNode = unbalancedNode
                gMap[unbalancedNode] = []
        for dictionaryKey in gMap:
            edges = gMap[dictionaryKey]
            if len(edges) != 1:
                for i in range(len(edges)):
                    if listKey == edges[i]:
                        incomingEdges += 1
            else:
                if listKey == edges[0]:
                    incomingEdges += 1
# Find unbalanced nodes
        if len(outgoingEdges) - incomingEdges == 1:
            unbalancedOutInNode = listKey
            activeNode = listKey
            cycle.append(activeNode)
        if incomingEdges - len(outgoingEdges) == 1:
            unbalancedInOutNode = listKey
            unbalancedNode = listKey
# Connect nodes in gMap
    gMap[unbalancedNode].append(activeNode)
# execute eulerian cycle
    eulerianCycle = construct_eulerian_cycle(gMap)
# Conversion of eulerian cycle to eulerian path requires rearrangement of
# euleriancycle
    for i in range(len(eulerianCycle)-1):
        if i == len(eulerianCycle):
            break
        if eulerianCycle[i] == unbalancedInOutNode and eulerianCycle[i+1] == unbalancedOutInNode:
            eulerianPath = eulerianCycle[i+1:] + eulerianCycle[1:i+1]
            return eulerianPath

def construct_eulerian_cycle(gMap):
    node = next(iter(gMap))
    cycle = []
    cycle.append(node)
    while len(gMap) > 0:
        if node in gMap:
            steps = gMap[node]
            step = steps[0]
            cycle.append(step)
            if len(steps) > 1:
                del gMap[node][0]
            else:
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
'''

import sys
import re
import heapq
import random
import numpy as np
from itertools import *
from collections import Counter,defaultdict

def de_bruijn(patterns):
    d = {}
    result = []
    for text in patterns:
        if text[:-1] not in d.keys():
            d[text[:-1]] = [text[1:]]
        else:
            d[text[:-1]].append(text[1:])
    for i in d:
        res = i+" -> "
        for j in d[i]:
            res+=j+","
        result.append(res[:-1])
    return result

def find_ender(data):
    item0 = [item[0] for item in data]
    item1 = [item[1] for item in data]
    c0 = Counter(item0)
    c1 = Counter(item1)
    result = [(item,c0[item],c1[item]) for item in c1 if c0[item] != c1[item]]
    return [item[0] for item in result if item[1] < item[2]][0]

def find_path(data):
    initial_ender = find_ender(data)
    ender = find_ender(data)
    path = [ender]
    while len(data) != 0:
        try:
            starter = [item1 for [item1,item2] in data if item2 == ender][0]
            data.remove([starter,ender])
            path.append(starter)
            ender = starter
        except:
            break
    return path[::-1]

def form_string(path):
    string = path[0]
    for item in path[1:]:
        string += item[-1]
    return string

def result(data):
    path = find_path(data)
    results = form_string(path)
    return results

if __name__ == "__main__":
    #k = int(sys.stdin.readline().strip())
    #patterns = [line.strip() for line in sys.stdin if line.strip()]
    
    k = int(input())
    patterns = []
    my = input()
    patterns.append(my)
    while(len(my)>0):
        my = input()
        patterns.append(my)
    patterns.pop(-1)
    '''
    results = de_bruijn(patterns)
    
    gMap = {}
    for i in range(len(results)):
        delimiter = ' -> '
        nodes = results[i].split(delimiter)
        for j in range(1, len(nodes)):
            delimiter = ','
            outNodes = nodes[j].split(delimiter)
            gMap[nodes[0]] = outNodes

    path = construct_eulerian_path(gMap)
    res = path[0]
    for i in range(1,len(path)):
        res += path[i][-1]
    print(res)
    '''
    results = de_bruijn(patterns)
    results_ = []
    for i in range(len(results)):
        l = results[i].split(' -> ')
        results_.append(l)
    print(results_)
    print(result(results_))