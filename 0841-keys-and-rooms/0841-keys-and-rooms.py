class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        
        def DFS(v):
            visited[v] = True
            for i in rooms[v]:
                if not visited[i]:
                    visited[i] = True
                    DFS(i)
            
        DFS(0)
        
        for i in range(n):
            if not visited[i]:
                return False
        
        return True