import graph as g
import math
# asumsi tidak ada simpul dengan nama yang sama bertetanggaan dengan simpul yang sama
# format file:
'''
<jumlah simpul (n)>
<nama simpul 1>,<lintang>,<bujur>
<nama simpul 2>,<lintang>,<bujur>
...
<nama simpul n>,<lintang>,<bujur>
<matriks ketetanggaan>
'''

class parsed:
    # nodes untuk menyimpan list of tuple yang berupa nama node, latitude, longitude
    def __init__(self, nodes, adjMatrix):
        self.nodes = nodes
        self.adjMatrix = adjMatrix

def parse(file):
    nodes = list()
    adjMatrix = list()
    
    totalNodes = int(file.readline().rstrip())  # membaca jumlah simpul

    temp = file.readlines()
    i = 0
    for line in temp:
        if i < totalNodes:                      # membaca nama, latitude, dan longitude n buah simpul
            line = line.rstrip().split(',')
            nodes.append(tuple(line))
        else:                                   # membaca adjacency matrix
            line = line.rstrip().split(' ')
            adjMatrix.append(list(line))
        i += 1

    return parsed(nodes, adjMatrix)

def getDistance(latA, longA, latB, longB):      # rumus Haversine
    latA = float(latA)
    longA = float(longA)
    latB = float(latB)
    longB = float(longB)
    R = 6371                                    # radium bumi dalam satuan km
    dLat = deg2rad(latB-latA)
    dLon = deg2rad(longB-longA)
    a = math.sin(dLat/2)**2 + math.cos(deg2rad(latA)) * math.cos(deg2rad(latB)) * math.sin(dLon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def deg2rad(deg):
    return deg * (math.pi/180)

def makeGraph(parsedInput):                     # membuat graph yang berupa list of node
    graph = list()
    index = int()
    for adjArray in parsedInput.adjMatrix:      # membaca ajadcency matrix
        n = parsedInput.nodes[index]            # menyimpan node yang berupa tuple
        adjNodes = dict()
        i = int()
        for n1 in adjArray:
            if int(n1) == 1:                    # untuk setiap node tetangga
                key = parsedInput.nodes[i]      # menyimpan dictionary node tetangga dengan key
                                                # berupa tuple nama, lat, long dan value berupa distance
                temp = dict([(key, getDistance(n[1], n[2], key[1], key[2]))])
                adjNodes.update(temp)
            i += 1
        graph.append(g.node(n[0], n[1], n[2], adjNodes))
        index += 1
    return graph
