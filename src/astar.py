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
            if ((x[1],x[2]) not in visited):
                tetangga.append(float(source.cost + y + getDistance(x[1],x[2],target.name[1],target.name[2]))) # Masukan nilai kedalam list
                tetangga.append(x)   # Jika iya maka perbandingkan value g(n) + h(n)

                if (len(searchNode(x,graph).path) == 0):
                    searchNode(x,graph).path.extend(before.path)
                else :
                    # Path sudah ada isinya, cek jalur mana yang lebih efisien
                    if (searchNode(x,graph).cost > source.cost + y):
                        searchNode(x,graph).path.clear()
                        searchNode(x,graph).path.extend(source.path)
                        searchNode(x,graph).cost = source.cost
                        # hasiltetangga.remove(x)
                        if (countX(hasiltetangga,x) > 1):
                            hasiltetangga.remove(getTetanggaTerlama(hasiltetangga,x))

                if (x[0] not in searchNode(x,graph).path):
                    searchNode(x,graph).path.append(x[0])

                if (searchNode(x,graph).cost == 0):
                    searchNode(x,graph).cost += (source.cost + y)
                else :
                    searchNode(x,graph).cost = (source.cost + y)
            if (len(tetangga) != 0):
                hasiltetangga.append(tetangga)

        # hasiltetangga = sorted(hasiltetangga, key=lambda x: x[0])
        hasiltetangga.sort(reverse=True)
        # print(hasiltetangga[len(hasiltetangga)-1][0],hasiltetangga[len(hasiltetangga)-1][1].name[0])

        # if (len(hasiltetangga[len(hasiltetangga)-1][1].path) == 0):
        #     hasiltetangga[len(hasiltetangga)-1][1].path.extend(source.path)

        # if (hasiltetangga[len(hasiltetangga)-1][1].name[0] not in hasiltetangga[len(hasiltetangga)-1][1].path):
        #     hasiltetangga[len(hasiltetangga)-1][1].path.append(hasiltetangga[len(hasiltetangga)-1][1].name[0])

        source = searchNode(hasiltetangga[len(hasiltetangga)-1][1],graph)
        before = source
        hasiltetangga.pop()
        if (source.name == target.name):
            found = True
    result.extend(source.path)
    result.append(str(source.cost))
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

def getTetanggaTerlama(a,x):
    max = a[0]
    for i in a:
        if (i[0] > max and i[1][0] == x):
            max = i
    return max

def countX(a,x):
    count = 0
    for i in a:
        if (i[1][0] == x[0]):
            count +=1
    return count
