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

class parsed:
    # nodes untuk menyimpan list of tuple yang berupa nama node, latitude, longitude
    def __init__(self, nodes, adjMatrix):
        self.nodes = nodes
        self.adjMatrix = adjMatrix

def parse(filename):
    nodes = list()
    adjMatrix = list()
    
    f = open('../test/' + filename, 'r')        # file harus berada di folder test
    totalNodes = int(f.readline().rstrip())     # membaca jumlah simpul

    temp = f.readlines()[0:totalNodes]          # membaca n jumlah simpul
    for line in temp:
        line = line.rstrip().split(' - ')
        line[1] = line[1].split(', ')
        temp = line[0], line[1][0], line[1][1]  # nama, latitude, longitude
        nodes.append(tuple(temp))
    f.close()

    f = open('../test/' + filename, 'r')        # membaca adjacency matrix
    temp = f.readlines()[totalNodes+1:totalNodes+1+totalNodes]
    for line in temp:
        line = line.rstrip().split(' ')
        adjMatrix.append(list(line))
    f.close()

    return parsed(nodes, adjMatrix)

def getDistance(latA, longA, latB, longB):      # rumus Haversine
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

def makeGraph(parsedInput):                     # membuat graph yang berupa list of node
    graph = list()
    index = int()
    for adjArray in parsedInput.adjMatrix:
        n = parsedInput.nodes[index]            # menyimpan node yang berupa tuple
        adjNodes = dict()
        i = int()
        for n1 in adjArray:
            if int(n1) == 1:
                key = parsedInput.nodes[i]
                temp = dict([(key, getDistance(n[1], n[2], key[1], key[2]))])
                adjNodes.update(temp)
            i += 1
        graph.append(g.node(n[0], n[1], n[2], adjNodes))
        index += 1
    return graph

# test = parse('test.txt')
# graph = makeGraph(test)

# for n in graph:
#     print(n.name[0], end=": ")
#     for o, dist in n.adjacentNodes.items():
#         # print(dist)
#         print('{} ({:.2f} km)'.format(o[0], dist), end="; ")
#     print()
