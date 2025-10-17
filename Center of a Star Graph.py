def find_center(edges):
    """
    Function to find the center node of the star graph.
    
    :param edges: List[List[int]] -> List of edges connecting the nodes
    :return: int -> The center node
    """
    # TODO: Implement the logic to find the center node
    edge1, edge2 = edges[0], edges[1]
    return edge1[0] if edge1[0] in edge2 else edge1[1]
