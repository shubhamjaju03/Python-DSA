  class GraphUsingEdgeList:
    def __init__(self):
        self.V = []
        self.edges = []
        self.vertices = self.V

    def add_vertex(self, vertex):
        if vertex not in self.V:
            self.V.append(vertex)
        else:
            print(f"Vertex {vertex} already exists")

    def add_edge(self, source, destination, weight=1):
        if source not in self.V or destination not in self.V:
            print("One or both the vertices are not found")
            return
        self.edges.append((source, destination, weight))

    def display(self):
        print("Vertices:")
        for vertex in self.V:
            print(f"Vertex: {vertex}")
        print("Edges:")
        for source, destination, _weight in self.edges:
            print(f"{source} ---> {destination}")
