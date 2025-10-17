def all_paths_source_target(graph):
    def dfs(node, path):
        if node == len(graph) - 1:
            res.append(path[:])
            return
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()

    res = []
    dfs(0, [0])
    return res
