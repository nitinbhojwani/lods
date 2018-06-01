class Graph:

    def __init__(self):
        self.graph_dict = {}

    def get_vertices(self):
        """ returns the vertices in graph """
        return list(self.graph_dict.keys())

    def get_edges(self):
        """ returns the edges in graph """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]
        if vertex2 in self.graph_dict:
            self.graph_dict[vertex2].append(vertex1)
        else:
            self.graph_dict[vertex2] = [vertex1]

    def bfs(self, search_input):
        """ A function that will do Breadth First Traversal and
            search search_input and return bool value
        """
        try:
            start_node = next(iter(self.graph_dict))
        except StopIteration as e:
            return False
        from pyqueue.queue import Queue
        queue = Queue()
        visited = set()
        queue.enqueue(start_node)
        while(not queue.is_empty()):
            current_node = queue.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                if current_node == search_input:
                    return True
                adjacent_nodes = self.graph_dict[current_node]
                for node in adjacent_nodes:
                    if node not in visited:
                        queue.enqueue(node)
        return False

    def dfs(self, search_input):
        """ A function that will do Depth First Traversal and
            search search_input and return bool value
        """
        try:
            start_node = next(iter(self.graph_dict))
        except StopIteration as e:
            return False
        from stack.stack import Stack
        stack = Stack()
        visited = set()
        stack.push(start_node)

        while (not stack.is_empty()):
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                if current_node == search_input:
                    return True
                adjacent_nodes = self.graph_dict[current_node]
                for node in adjacent_nodes:
                    if node not in visited:
                        stack.push(node)
        return False

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.get_edges():
            res += str(edge) + " "
        return res
