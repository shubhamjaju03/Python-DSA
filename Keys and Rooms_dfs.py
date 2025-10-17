def can_visit_all_rooms(rooms):
    visted=[False]*len(rooms)
    
    def dfs(room):
        if visted[room]:
            return
        visted[room]=True
        for key in rooms[room]:
            dfs(key)
    dfs(0)
    return all(visted)
