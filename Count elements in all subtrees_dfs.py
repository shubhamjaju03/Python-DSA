def countSubtreeNodes(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    subtree_sizes = [0] * n
    
    def dfs(node, parent):
        size = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                size += dfs(neighbor, node)
        subtree_sizes[node] = size
        return size
    
    dfs(0, -1)
    
    return subtree_sizes
