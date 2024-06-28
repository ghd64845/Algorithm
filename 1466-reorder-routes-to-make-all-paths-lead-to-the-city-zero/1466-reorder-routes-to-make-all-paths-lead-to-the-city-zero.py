class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [False] * (n)
        graph = [[] for _ in range(n)]
        s = set()
       
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            s.add((a, b))
            
        def DFS(v):
            visited[v] = True
            ans = 0
            for i in graph[v]:
                if not visited[i]:
                    if (v, i) in s:
                        ans += 1
                    ans += DFS(i)
            return ans
        
        return DFS(0)
            
        
        
        # 0 1
        # 1 3
        # 2 3
        # 3 
        # 4 0 5
        # 5
