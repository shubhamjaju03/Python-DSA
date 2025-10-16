class GraphAdjacencyMatrix:
    
    def __init__(self, num_vertices):
        self.num_vertices=num_vertices
        self.vertices=[None]*num_vertices
        self.adj_matrix=[[0]* num_vertices for row in range(num_vertices)]

    def add_vertex(self, index, label):
        if ( index>=0  and index<self.num_vertices):
            self.vertices[index]=label
        else:
            print("Index OOB")

    def add_edge(self, source, destination, weight=1):
        # Add your code here
        if 0 <= source < self.num_vertices and 0 <= destination <self.num_vertices:
            self.adj_matrix[source][destination]=weight
            self.adj_matrix[destination][source]=weight
            

    def display(self):
        # Print vertex labels
        print("Vertices:", self.vertices)
        print("Adjacency Matrix:")
        for i in range(self.num_vertices):
            print(self.adj_matrix[i])
