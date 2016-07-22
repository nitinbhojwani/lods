class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def bfs(self, search_input):
        """ A function that will do Breadth First Traversal and
            search search_input and return bool value
        """
        from queue import Queue
        queue = Queue()
        visited = {}
        queue.enqueue(self.__graph_dict.keys()[0])        
        while (!queue.is_empty):
            current_node = queue.dequeue()
            if not visited.get(current_node):
                visited[current_node] = True
            """ Below written code helps in termination """    
            if current_node == search_input:
                return True
            adjacent_nodes = self.__graph_dict[current_node]
            for node in adjacent_nodes:
                queue.enqueue(node)
        return False

    def dfs(self, search_input):
        """ A function that will do Depth First Traversal and
            search search_input and return bool value
        """
        from stack import Stack
        stack = Stack()

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
