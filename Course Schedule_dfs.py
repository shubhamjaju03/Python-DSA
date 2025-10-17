def can_finish_courses(N, prerequisites):
    graph = build_graph(N, prerequisites)
    visited = [0] * (N + 1)
    
    def dfs(course):
        if visited[course] == 1:  
            return False
        if visited[course] == 2:
            return True
        
        visited[course] = 1  
        for next_course in graph[course]:
            if not dfs(next_course):
                return False
        visited[course] = 2 
        return True
    
    for c in range(1, N + 1):
        if visited[c] == 0 and not dfs(c):
            return False
    return True

def build_graph(N, prerequisites):
    graph = {i: [] for i in range(1, N + 1)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    return graph
