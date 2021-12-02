# Importer les librairie necessaires pour visualiser le graph

import networkx as nx
import matplotlib.pyplot as plt
from  collections import defaultdict

# Créer la class du vestibule qui contient son nom, taille et une fonction pour commencer le jeu

class Vestibule:
    def __init__(self,name, size,capacity):
        self.name = name
        self.size = size
        self.capacity = capacity

    def getSize(self):
        return size

    def getName(self):
        return self.name

    def start(self, ants):
        self.ants = ants
        ants = self.size
        print("There are ", ants, " ants in the vestibule")
        print("----------------------")
        return ants


# Créer la class du vestibule qui contient son nom, taille et une fonction pour commencer le jeu

class Salles:
    def __init__(self,name,size,capacity):
        self.name = name
        self.size = size
        self.capacity = capacity

    def getRooms(self):
        x = dict(zip(self.name, self.size))
        return x

    def getRoomCapacity(self):
        y = dict(zip(self.size,self.capacity))
        return y


# La class qui contient le nom et la taille du dortoire

class Dorm:
    def __init__(self,name,size,capacity):
        self.name = name
        self.size = size
        self.capacity = capacity

# Définir les paramêtres

size = 10

Sv = Vestibule("Sv",size,size)
Sv.start(size)
salles = Salles(("S1","S2","S3","S4","S5","S6"),(0,0,0,0,0,0),(2,1,1,2,1,1))
dorm = Dorm("Sd",0,size)


#Créer la fonction qui va établir toutes les connections entre chaques salle et toutes les autre

def buildGraph():
    edges = [
        [salles.name[2],salles.name[3]],
        [Sv.name, salles.name[0]],
        [salles.name[0], salles.name[1]],
        [salles.name[1], salles.name[3]],
        [salles.name[3], salles.name[4]],
        [salles.name[4], dorm.name],
        [salles.name[3], salles.name[5]],
        [salles.name[5], dorm.name],
        [salles.name[0], salles.name[2]],
    ]
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]

        graph[a].append(b)
        graph[b].append(a)
    return graph

if __name__ == "__main__":
    g = buildGraph()

# Créer la fonction qui détermine le chemin le plus court en commençant par le vestibule et arrivant au dortoir

def shortestPath(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                newPath = list(path)
                newPath.append(neighbour)
                queue.append(newPath)
                if neighbour == goal:
                    return list(newPath)
            explored.append(node)

if __name__ == "__main__":
    Sp = shortestPath(g, "Sv", "Sd")

# Créer la classe des fourmilles qui a comme attribut toutes les salles et qui contient la fonction qui déplace les fourmilles
# Créer une matrice qui contient les tailles et capacités de chaque salle
# Créer pour chaqu'un des salle (vestibule et dortoir inclus) une fonction qui fait rentrer et sortir les fourmis
# en utilisant la récursivité

class Ant:
    def __init__(self, ant, vestibule, rooms, dorm, capacity):
        self.ant = ant
        self.vestibule = vestibule
        self.rooms = rooms
        self.dorm = dorm
        self.capacity = capacity
        self.vestibule = Vestibule("Sv", self.ant,size)
        a = Vestibule.getSize(self.vestibule)
        ant = a
        s = Salles.getRooms(self.rooms)
        rooms = s
        c = Salles.getRoomCapacity(self.rooms)
        capacity = c
        d = Dorm("Sd", 0,size)
        dorm = d.name
        self.dormSize = d.size

        self.newHallways = []
        self.newHallways.append((Sp[0], Sp[1]))
        self.newHallways.append((Sp[1], Sp[2]))
        self.newHallways.append((Sp[2], Sp[3]))
        self.newHallways.append((Sp[3], Sp[4]))
        self.newHallways.append((Sp[4], Sp[5]))
        print("Shortest way is: ",self.newHallways)



    def nodesMatrix(self):

        matrix = []
        matrix.append([self.vestibule.size,self.vestibule.size])
        matrix.append([self.rooms.size[0],self.capacity[0]])
        matrix.append([self.rooms.size[1],self.capacity[1]])
        matrix.append([self.rooms.size[3],self.capacity[3]])
        matrix.append([self.rooms.size[4],self.capacity[4]])
        matrix.append([self.dormSize,self.vestibule.size])
        return matrix

    def ves(self,a):
        self.a = a
        if matrix[0][0] > 0:
            return True
        else:
            return False
    def salle1(self):

        if self.ves(self.a) == True:
            if matrix[1][0] == 0:
                matrix[1][0] = matrix[1][1]
                matrix[0][0] -= matrix[1][0]
                print(matrix[1][0], " ants ",self.vestibule.name, " -----> ", self.rooms.name[0])
                self.a -= matrix[1][0]
                print("Sv ",self.a," ants")
            elif matrix[1][0] == 1:
                matrix[1][0] += 1
                matrix[0][0] -= 1
                print(1, " ant ", self.vestibule.name," -----> ",self.rooms.name[0])
                self.a -= 1
                print("Sv ",self.a," ants")
        else:
            pass

    def salle2(self):
        if matrix[1][0] > 0:
            matrix[2][0] = matrix[2][1]
            matrix[1][0] -= matrix[2][0]
            print(matrix[2][0], " ant ", self.rooms.name[0]," -----> ",self.rooms.name[1])
            self.salle1()
        elif matrix[1][0] == 0:
            pass

    def salle4(self):
        if matrix[2][0] > 0:
            if matrix[3][0] == 0:
                matrix[3][0] = matrix[2][0]
                matrix[2][0] -= matrix[3][0]
                print(matrix[3][0], " ant ", self.rooms.name[1], " -----> ", self.rooms.name[3])
                self.salle2()
                matrix[3][0] +=1
                print(matrix[2][1], " ant ", self.rooms.name[1], " -----> ", self.rooms.name[3])
                self.salle2()
            elif matrix[3][0] == 1:
                matrix[3][0] += 1
                matrix[2][0] -= 1
                print(matrix[2][1],' ant ',self.rooms.name[1]," -----> ",self.rooms.name[3])
                self.salle2()



        elif matrix[2][0] == 0:
            pass

    def salle5(self):
        if matrix[3][0] > 0:
            matrix[4][0] = matrix[4][1]
            matrix[3][0] -= matrix[4][0]
            print(matrix[4][0]," ant ", self.rooms.name[3]," -----> ",self.rooms.name[4])
            self.salle4()
        elif matrix[3][0] == 0:
            pass

    def Sd(self,steps):
        if matrix[4][0] == 1:
            matrix[5][0] += 1
            matrix[4][0] -= 1
            print(matrix[4][1]," ant ",self.rooms.name[4]," -----> ",dorm.name)
            self.salle5()
            steps += 1
            print("Step ",steps)
            print(matrix[4][1]," ant ",self.rooms.name[4]," -----> ",dorm.name)
            matrix[5][0] += 1
            self.salle5()
            steps += 1
            print("Step ", steps)
            print(matrix[4][1], " ant ", self.rooms.name[4], " -----> ", dorm.name)
            matrix[5][0] += 1
            self.salle5()
            steps += 1
            print("Step ", steps)
            print(matrix[4][1], " ant ", self.rooms.name[4], " -----> ", dorm.name)
            matrix[5][0] += 1
            self.salle5()
            steps += 1
            print("Step ", steps)
            print(matrix[4][1], " ant ", self.rooms.name[4], " -----> ", dorm.name)
            matrix[5][0] += 1
            self.salle5()
            steps += 1
            print("Step ", steps)
            print(matrix[4][1], " ant ", self.rooms.name[4], " -----> ", dorm.name)
            matrix[5][0] += 1
            self.salle5()
            steps += 1
            print("Step ", steps)
            print(matrix[4][1], " ant ", self.rooms.name[4], " -----> ", dorm.name)
            matrix[5][0] += 1
            self.salle5()
            steps += 1
            print("Step ", steps)
            print(matrix[4][1], " ant ", self.rooms.name[4], " -----> ", dorm.name)
            matrix[5][0] += 1
            self.salle5()
            steps += 1
            print("Step ", steps)
            print(matrix[4][1], " ant ", self.rooms.name[4], " -----> ", dorm.name)
            matrix[5][0] += 1
            self.salle5()
            steps += 1
            print("Step ", steps)
            print(matrix[4][1], " ant ", self.rooms.name[4], " -----> ", dorm.name)
            matrix[5][0] += 1
            print("------------------")
            print("Sv ", self.a," ants ")
            print("Sd ",matrix[5][0]," ants")
            if matrix[5][0] == matrix[5][1]:
                print("Game Over")






go = Ant(size,Sv.name,salles,dorm.name,salles.capacity)
matrix = go.nodesMatrix()
go.ves(size)
print("Step 1")
go.salle1()
print("Step 2")
go.salle2()
print("Step 3")
go.salle4()
print("Step 4")
go.salle5()
print("Step 5")
go.Sd(5)

# Créer la classe qui visualise la fourmillière en graph

class Anthill:
    def __init__(self):
        self.nodes = []
        self.edges = []
    def addNodes(self,a,b,c,d):
        nodes = [a,b,c,d]
        self.nodes.append(nodes)
    def addEdges(self,a,b):
        edges = [a,b]
        self.edges.append(edges)
    def visualizeGraph(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.nodes)
        graph.add_edges_from(self.edges)
        nx.draw_networkx(graph)
        plt.show()

graph = Anthill()
graph.addEdges(salles.name[2],salles.name[3])
graph.addEdges(Sv.name,salles.name[0])
graph.addEdges(salles.name[0],salles.name[1])
graph.addEdges(salles.name[1],salles.name[3])
graph.addEdges(salles.name[3],salles.name[4])
graph.addEdges(salles.name[4],dorm.name)
graph.addEdges(salles.name[3],salles.name[5])
graph.addEdges(salles.name[5],dorm.name)
graph.addEdges(salles.name[0],salles.name[2])

graph.visualizeGraph()















