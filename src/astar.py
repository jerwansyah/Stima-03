from parser import *

def astar(source,target,graph):
    result = []
    if (source.name[0] == target.name[0]):
        return [[],str(-1)]
    found = False    
    before = source
    source.path.append(source.name[0])
    visited = []
    hasiltetangga = []
    while (not found):
        visit = False
        visited.append((source.name[1],source.name[2]))
        for x,y in source.adjacentNodes.items():  # Iterasikan setiap node yang bertetanggaan
            tetangga = []
            if ((x[1],x[2]) not in visited):
                visit = True
                tetangga.append(float(source.cost + y + getDistance(x[1],x[2],target.name[1],target.name[2]))) # Masukan value g(n) + h(n) kedalam list
                tetangga.append(x)   # Masukkan data X kedalam list

                if (len(searchNode(x,graph).path) == 0): # Jika path masih kosong, maka path akan diisi dengan path source saat ini
                    searchNode(x,graph).path.extend(before.path)
                else :
                    # Path sudah ada isinya, cek jalur mana yang lebih efisien
                    if (searchNode(x,graph).cost > source.cost + y):
                        searchNode(x,graph).path.clear() # Kosongkan Path Node Tetangga
                        searchNode(x,graph).path.extend(source.path) # Isi Path Node tetangga dengan Node source
                        searchNode(x,graph).cost = source.cost # Ubah Cost Node tetangga dengan node Node source
                        if (countX(hasiltetangga,x) > 1):
                            # Jika ada 2 buah Node dengan Nama yang sama, maka hanya 1 node yang akan dibandingkan
                            # Dan Salah satu Node dengan f(n) lebih besar maka node tersebut akan dihapus
                            hasiltetangga.remove(getTetanggaTerlama(hasiltetangga,x))

                if (x[0] not in searchNode(x,graph).path): # Jika pada path, nama node belum ada, maka node akan dimasukkan
                    searchNode(x,graph).path.append(x[0])

                if (searchNode(x,graph).cost == 0):                     # Jika pada node tetangga, nilai cost masih bernilai 0, 
                    searchNode(x,graph).cost += (source.cost + y)       # maka nilai node tersebut akan diset menjadi cost dari node source
                else :                                                  # Jika pada node tetangga nilai cost tidak bernilai 0, 
                    searchNode(x,graph).cost = (source.cost + y)        # maka nilai node tersebut akan ditimpa oleh cost dari node source
            if (len(tetangga) != 0):
                hasiltetangga.append(tetangga) # hasiltetangga akan diappend dengan tetangga dengan syarat tetangga bukan list kosong

        if (not visit and len(hasiltetangga)==0): # Jika Semua graf sudah dikunjungi, namun node destination masih belum bisa ditemukan
            return [[],str(-2)]                   # Maka akan mereturn list kosong yang akan ditangkap dan dihandle oleh App.py

        hasiltetangga.sort(reverse=True) # Melakukan sorting
        source = searchNode(hasiltetangga[len(hasiltetangga)-1][1],graph) # Mengambil Nilai dengan cost terendah
        before = source 
        hasiltetangga.pop() 
        if (source.name == target.name): # Target sudah ditemukan, algoritma akan berhenti
            found = True
    result = [source.path.copy(),source.cost] # Melakukan copy untuk mereturn
    clean(graph) # Membersihkan setiap bentuk graph (path menjadi kosong, dan cost bernilai 0)
    return result # Melakukan pengembalian Path dan Cost untuk ditampilkan

def searchNode(name,graph): # Mencari Node dengan nama dan koordinat latitude dan longitude
    for i in graph:
        if i.name[1] == name[1] and i.name[2] == name[2]:
            return i

def clean(graph): # Membersihkan setiap bentuk graph (path menjadi kosong, dan cost bernilai 0)
    for i in graph:
        i.path.clear()
        i.cost = 0  

def getTetanggaTerlama(a,x): # mengembalikan Node dengan f(n) terbesar 
    max = a[0]
    for i in a:
        if (i[0] > max[0] and i[1][0] == x):
            max = i
    return max

def countX(a,x): # Menghitung jumlah x pada graph a
    count = 0
    for i in a:
        if (i[1][0] == x[0]):
            count +=1
    return count
