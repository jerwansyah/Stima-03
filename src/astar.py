from parser import *

def astar(source,target,graph):
    found = False    
    before = source
    source.path.append(source.name[0])
    visited = []
    result = []
    hasiltetangga = []
    while (not found):
        visited.append((source.name[1],source.name[2]))
        for x,y in source.adjacentNodes.items():  # Iterasikan setiap node yang bertetanggaan
            tetangga = []
            # print("--------------------------------Visited--------------------------------")
            # print(visited)
            # print("--------------------------------x[1] dan x[2]--------------------------------")
            # print (x[1],x[2])
            if ((x[1],x[2]) not in visited):
                tetangga.append(float(before.cost + y + getDistance(x[1],x[2],target.name[1],target.name[2]))) # Masukan nilai kedalam list
                tetangga.append(x)   #Jika iya maka perbandingkan value g(n) + h(n)
                # source.cost = before.cost + y
                # print()
                # print(before.path)
                # print(searchNode(x,graph).path)
                if (len(searchNode(x,graph).path) == 0):
                    searchNode(x,graph).path.extend(before.path)
                # print(searchNode(x,graph).path)
                if (x[0] not in searchNode(x,graph).path):
                    searchNode(x,graph).path.append(x[0])
                # print(searchNode(x,graph).path)
                # print(searchNode(x,graph).path)
            if (len(tetangga) != 0):
                hasiltetangga.append(tetangga)
        hasiltetangga.sort(reverse=True)
        # print(hasiltetangga)
        # if (before.path[len(before.path)-1] == source.path[len(source.path)-1]) :
        #     source.path.extend(before.path)
        # source.path.append(source.name[0])
        # print(source.path)
        before.cost += hasiltetangga[len(hasiltetangga)-1][0]
        source = searchNode(hasiltetangga[len(hasiltetangga)-1][1],graph)
        before = source
        # print("------------")
        # print(before.path)
        # Ngambil graf dengan nama hasiltetangga[len(hasiltetangga)-1][1]
        hasiltetangga.pop()
        # print(hasiltetangga)
        # if (source.name[0] not in result):
        if (source.name == target.name):
            found = True
    result.extend(source.path)
    clean(graph)
    return result

def searchNode(name,graph):
    for i in graph:
        if i.name[1] == name[1] and i.name[2] == name[2]:
            return i

def clean(graph):
    for i in graph:
        i.path.clear()
        i.cost = 0  

graph = makeGraph(parse('test.txt'))
# print(nodes)
# for i in graph :
#     print(i.adjacentNodes)

# for i,j in graph[0].adjacentNodes.items():
#     print (graph[0].name ,i,j)
# count=0
# result =[]
# for i in graph:
#     result.append(float(i.name[2]))
# print(result)
# print(astar(graph[1],graph[19],graph))
# print(astar(graph[1],graph[0],graph))
# print(astar(graph[0],graph[19],graph))
# print(astar(graph[0],graph[16],graph))
# print(astar(graph[3],graph[8],graph))
# for i in graph:
#     for x,y in i.adjacentNodes.items():
#         print(x[1],x[2])
#     print()
# clean(graph)
# 1 19
# 0 1
# 0 19
# 19 16
# 3 8
# for i in graph:
#     for x,y in i.adjacentNodes.items():
#         print(i.name[0],end = " ") 
#         print(x[0])
# a = ('44.457', '26.093')
# for i in graph:
#     # print(i.name)
#     if a == i.name:
#         print(i) 

