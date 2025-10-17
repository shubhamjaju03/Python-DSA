def find_circle_num(is_connected):
    n = len(is_connected)
    visited = [False] * n
    count = 0

    def dfs(city):
        for adj_city in range(n):
            if is_connected[city][adj_city] == 1 and not visited[adj_city]:
                visited[adj_city] = True
                dfs(adj_city)

    for city in range(n):
        if not visited[city]:
            visited[city] = True
            dfs(city)
            count += 1

    return count
