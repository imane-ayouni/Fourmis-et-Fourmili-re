# Importer les librairie necessaires pour visualiser le graph

import networkx as nx
import matplotlib.pyplot as plt


# Créer la class du vestibule qui contient son nom, taille et une fonction pour commencer le jeu

class Vestibule:
    def __init__(self, name, size):
        self.name = name
        self.size = size

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


# Créer la class des salles sui contient les nom, tailles et une fonction qui obtient les couloirs ou les fourmilles pouvent se déplacer

class Salles:
    def __init__(self, name, size, capacity):
        self.name = name
        self.size = size
        self.capacity = capacity
        self.rooms = dict(zip(self.name, self.size))

    def getRooms(self):
        x = dict(zip(self.name, self.size))
        return x


# Créer la classe des fourmilles qui a comme attribut toutes les salles et qui contient la fonction qui déplace les fourmilles
# Créer une matrice qui contient les tailles et capacités de chaque salle
# Créer pour chaqu'un des salle (vestibule et dortoir inclus) une fonction qui fait rentrer et sortir les fourmis
# en utilisant la récursivité

class Ant:
    def __init__(self, ant, vestibule, rooms, dorm):
        self.ant = ant
        self.vestibule = vestibule
        self.rooms = rooms
        self.dorm = dorm

        v = Vestibule("Sv", self.ant)
        vestibule = v.name
        a = Vestibule.getSize(self.vestibule)  # ant = how many ants in the entrance
        ant = a
        s = Salles.getRooms(self.rooms)
        rooms = s
        name = rooms.keys()
        size = rooms.values()
        self.dorm = Dorm("Sd", 0, size)

    def nodesMatrix(self):
        matrix = []
        matrix.append([Sv.size, Sv.size])
        matrix.append([salles.size[0], salles.capacity[0]])
        matrix.append([salles.size[1], salles.capacity[1]])
        matrix.append([dorm.size, dorm.capacity])
        print(matrix)
        return matrix

    def ves(self, a):
        self.a = a
        if matrix[0][0] > 0:
            return True
        else:
            return False

    def salle1(self):
        if self.ves(self.a) == True:
            matrix[1][0] = matrix[1][1]
            matrix[0][0] -= matrix[1][0]
            print(matrix[1][0], " ant ", self.vestibule, " -----> ", self.rooms.name[0])
            self.a -= 1
            print("Sv", self.a, " ants")
        else:
            pass

    def salle2(self):
        if matrix[1][0] == 1:
            matrix[1][0] -= 1
            matrix[2][0] = matrix[2][1]
            print(matrix[2][0], " ant ", self.rooms.name[0], " -----> ", self.rooms.name[1])
            self.salle1()

        elif matrix[1][0] == 0:
            pass

    def Sd(self, steps):
        if matrix[2][0] == 1:
            matrix[2][0] -= 1
            matrix[3][0] += 1
            print(matrix[2][1], " ant ", self.rooms.name[1], " -----> ", self.dorm.name)
            self.salle2()
            steps += 1
            print("Step ", steps)
            print(matrix[2][1], " ant ", self.rooms.name[1], " -----> ", self.dorm.name)
            matrix[3][0] += 1
            self.salle2()
            steps += 1
            print("Step ", steps)
            print(matrix[2][1], " ant ", self.rooms.name[1], " -----> ", self.dorm.name)
            matrix[3][0] += 1
            self.salle2()
            self.salle1()
            steps += 1
            matrix[3][0] += 1
            print("Step ", steps)
            print(matrix[2][1], " ant ", self.rooms.name[1], " -----> ", self.dorm.name)
            matrix[2][0] = 0
            self.salle2()
            steps += 1
            print("Step ", steps)
            matrix[3][0] += 1
            print(matrix[2][1], " ant ", self.rooms.name[1], " -----> ", self.dorm.name)
            print("------------------")
            print("Sv ", self.a, " ants")
            print("Sd ", matrix[3][0], " ants")
            if matrix[3][0] == matrix[3][1]:
                print("Game Over")


# La class qui contient le nom et la taille du dortoire
class Dorm:
    def __init__(self, name, size, capacity):
        self.name = name
        self.size = size
        self.capacity = capacity


# Définir les paramêtres

size = 5
Sv = Vestibule("Sv", size)
Sv.start(size)
salles = Salles(("S1", "S2"), (0, 0), (1, 1))
dorm = Dorm("Sd", 0, size)

go = Ant(size, Sv.name, salles, dorm.name)
matrix = go.nodesMatrix()
go.ves(size)
print("Step 1")
go.salle1()
print("Step 2")
go.salle2()
print("Step 3")
go.Sd(3)


# Créer la classe qui visualise la fourmillière en graph

class Anthill:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNodes(self, a, b, c, d):
        nodes = [a, b, c, d]
        self.nodes.append(nodes)

    def addEdges(self, a, b):
        edges = [a, b]
        self.edges.append(edges)

    def visualizeGraph(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.nodes)
        graph.add_edges_from(self.edges)
        nx.draw_networkx(graph)
        plt.show()


graph = Anthill()

graph.addEdges(Sv.name, salles.name[0])
graph.addEdges(salles.name[0], salles.name[1])
graph.addEdges(salles.name[1], dorm.name)

graph.visualizeGraph()
