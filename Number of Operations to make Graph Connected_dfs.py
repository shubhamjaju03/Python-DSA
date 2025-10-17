def minOperationsToConnectComputers(n, connections):
    if len(connections) < n - 1:
        return -1

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        rootA, rootB = find(a), find(b)
        if rootA != rootB:
            parent[rootA] = rootB
            return True
        return False

    components = n
    for a, b in connections:
        if union(a, b):
            components -= 1

    return components - 1
