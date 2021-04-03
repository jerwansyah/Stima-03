import graph as g
import math
# asumsi tidak ada simpul dengan nama yang sama bertetanggaan dengan simpul yang sama
# format file:
'''
<jumlah simpul (n)>
<nama simpul 1> - <lintang>, <bujur>
<nama simpul 2> - <lintang>, <bujur>
...
<nama simpul n> - <lintang>, <bujur>
<matriks ketetanggaan>
'''

nodes = dict()
nodeNames = list()
adjMatrix = list()
totalNodes = int()

def parse(filename):
    f = open('../test/' + filename, 'r')
    totalNodes = int(f.readline().rstrip())

    temp = f.readlines()[0:totalNodes]
    for line in temp:
        line = line.rstrip().split(' - ')
        line[1] = line[1].split(', ')
        temp = dict([(tuple(line[1]), line[0])])
        nodes.update(temp)
        nodeNames.append(line[0])
    f.close()

    f = open('../test/' + filename, 'r')
    temp = f.readlines()[totalNodes+1:totalNodes+1+totalNodes]
    for line in temp:
        line = line.rstrip().split(' ')
        adjMatrix.append(list(line))
    f.close()

def getDistance(latA, longA, latB, longB):
    latA = float(latA)
    longA = float(longA)
    latB = float(latB)
    longB = float(longB)
    R = 6371
    dLat = deg2rad(latB-latA)
    dLon = deg2rad(longB-longA)
    a = math.sin(dLat/2)**2+ math.cos(deg2rad(latA)) * math.cos(deg2rad(latB)) * math.sin(dLon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def deg2rad(deg):
    return deg * (math.pi/180)

def makeGraph():
    graph = list()
    index = int()
    for adjArray in adjMatrix:
        n = getKey(nodes, nodeNames[index])
        adjNodes = dict()
        i = int()
        for n1 in adjArray:
            if int(n1) == 1:
                key = getKey(nodes, nodeNames[i])
                temp = dict([(key, getDistance(n[0], n[1], key[0], key[1]))])
                adjNodes.update(temp)
            i += 1
        graph.append(g.node(n, adjNodes))
        index += 1
    return graph

def getKey(d, value):
    if value not in d.values():
        return None
    for key in d:
        if d[key] == value:
            return key

# parse('test.txt')
# graph = makeGraph()

# for n in graph:
#     print(nodes[n.name], end=": ")
#     for o, dist in n.adjacentNodes.items():
#         # print(dist)
#         print('{} ({:.2f} km)'.format(nodes[o], dist), end="; ")
#     print()