# Node data structure
class Node: 
    def __init__(self, vertex, square):        
        self.out_edges = []
        self.vertex_id = vertex
        self.square_id = square
        self.is_goal = False


    def add_edge(self, node, weight = 0):          
        self.out_edges.append(Edge(node, weight))

# Edge data structure
class Edge:

    def __init__(self, node, weight = 0):          
        self.node = node
        self.weight = weight

    def to(self):                                  
        return self.node

# Graph data structure, utilises classes Node and Edge
class Graph:    

    def __init__(self):
        self.nodes = []
        self.source = None

    def read_graph(self, filename):
        nodes = list()
        file = open(filename, 'r')
        line = file.readline()
        #read vertices and squares
        while(not line[0].isdigit()):
            line = file.readline()
        while(line[0].isdigit()):
            vertex, square = list(map(int, line.split(',')))
            nodes.append(Node(vertex, square))
            line = file.readline()
            if not line[0].isdigit():
                break
        #read edges
        while(not line[0].isdigit()):
            line = file.readline()
        while(line[0].isdigit()):
            a, b, dist = list(map(int, line.split(',')))
            nodes[a].add_edge(nodes[b], dist)
            nodes[b].add_edge(nodes[a], dist)
            line = file.readline()
        #read source and destination
        file.readline()
        source = int(file.readline().split(',')[1])
        destination = int(file.readline().split(',')[1])
        nodes[destination].is_goal = True

        self.nodes = nodes
        self.source = self.nodes[source]