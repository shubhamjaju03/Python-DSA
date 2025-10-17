def count_complete_components(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    count = 0

    def dfs(node):
        stack = [node]
        component_nodes = []
        edge_count = 0
        visited[node] = True

        while stack:
            curr = stack.pop()
            component_nodes.append(curr)
            for neighbour in graph[curr]:
                edge_count += 1
                if not visited[neighbour]:
                    visited[neighbour] = True
                    stack.append(neighbour)

        return component_nodes, edge_count // 2

    for i in range(n):
        if not visited[i]:
            nodes, edges_count = dfs(i)
            size = len(nodes)
            if edges_count == size * (size - 1) // 2:
                count += 1

    return count
