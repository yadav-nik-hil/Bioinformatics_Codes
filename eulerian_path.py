#python3

import sys
from collections import *

def construct_eulerian_path(gMap):
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
        if len(outgoingEdges) - incomingEdges == 1:
            unbalancedOutInNode = listKey
            activeNode = listKey
            cycle.append(activeNode)
        if incomingEdges - len(outgoingEdges) == 1:
            unbalancedInOutNode = listKey
            unbalancedNode = listKey
    gMap[unbalancedNode].append(activeNode)
    eulerianCycle = construct_eulerian_cycle(gMap)
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

# ---MAINCODE-----------------------------------------------------------
rawgMap = sys.stdin.read().splitlines()
'''
rawgMap = []
my = input()
rawgMap.append(my)
while(len(my)>0):
    my = input()
    rawgMap.append(my)
rawgMap.pop(-1)
'''
gMap = {}
for i in range(len(rawgMap)):
    delimiter = ' -> '
    nodes = rawgMap[i].split(delimiter)
    for j in range(1, len(nodes)):
        delimiter = ','
        outNodes = nodes[j].split(delimiter)
        gMap[nodes[0]] = outNodes

path = construct_eulerian_path(gMap)
print("->".join(path))