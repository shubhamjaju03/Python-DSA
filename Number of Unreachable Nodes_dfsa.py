def count_unreachable_pairs(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    component_sizes = []

    def dfs(node):
        stack = [node]
        size = 0

        while stack:
            curr = stack.pop()
            if not visited[curr]:
                visited[curr] = True
                size += 1
                for neighbor in graph[curr]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return size

    for i in range(n):
        if not visited[i]:
            size = dfs(i)
            component_sizes.append(size)

    total = 0
    sum_so_far = 0

    for sz in component_sizes:
        total += sz * sum_so_far
        sum_so_far += sz

    return total
