#python3
import sys
import timeit
import re
import heapq
import random
import numpy as np
from scipy import stats
from itertools import *
from collections import Counter,defaultdict

def data_process(line):
    line = [item.strip() for item in line.split('->')]
    if ',' in line[1]:
        for item in line[1].split(','):
            line.append((line[0],item))
        line.pop(0)
        line.pop(0)
    else:
        line = tuple(line)
    return line

def form_cycle(data):
    rgk,rgv = random.choice(data)
    cycle = [rgk]
    while len(data) != 0:
        try:
            cycle.append(rgv)
            data.remove((rgk,rgv))
            rgk = rgv
            rgv = [item2 for (item1,item2) in data if rgv == item1][0]
        except:
            break
    return (cycle,data)

def form_unCycle(data,rgk):
    rgv = [item2 for (item1,item2) in data if rgk == item1][0]
    cycle = [rgk]
    while len(data) != 0:
        try:
            cycle.append(rgv)
            data.remove((rgk,rgv))
            rgk = rgv
            rgv = [item2 for (item1,item2) in data if rgv == item1][0]
        except:
            break
    return (cycle,data)

def fuse(Cycle,new_Cycle):
    fuse_index = Cycle.index(new_Cycle[0])
    return Cycle[:fuse_index]+new_Cycle+Cycle[fuse_index+1:]

def eulerian_cycle(data):
    Cycle,unCycle = form_cycle(data)
    while len(unCycle) != 0:
        potential = [item for item in Cycle if item in chain(*unCycle)]
        newStart = random.choice(potential)
        new_Cycle,unCycle = form_unCycle(unCycle,newStart)
        Cycle = fuse(Cycle,new_Cycle)
    return Cycle

def result(graph):
    results = eulerian_cycle(graph)
    return results


if __name__ == "__main__":
    #graph = sys.stdin.read().strip().splitlines()
    
    graph = []
    my = input()
    graph.append(my)
    while(len(my)>0):
        my = input()
        graph.append(my)
    graph.pop(-1)
    
    result_ = []
    for line in graph:
        dp = data_process(line)
        if isinstance(dp,tuple):
            result_.append(dp)
        elif isinstance(dp,list):
            result_ += dp
    
    results = result(result_)
    print('->'.join(results))
