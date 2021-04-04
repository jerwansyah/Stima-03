class node:
    # Kelas node dengan atribut nama node dan dictionary node tetangga
    def __init__(self, name, lat, long, adjacentNodes):
        self.name = name, lat, long
        self.adjacentNodes = adjacentNodes
        self.cost = 0
        self.path = []
