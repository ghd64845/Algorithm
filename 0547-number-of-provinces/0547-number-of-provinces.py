class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        cnt = 0
        
        def DFS(v):
            visited[v] = True
            for idx, n in enumerate(isConnected[v]):
                if idx == v:
                    continue
                else:
                    if n == 1 and not visited[idx]:
                        DFS(idx)
            
        
        for i in range(n):
            if not visited[i]:
                cnt += 1
                DFS(i)
        
        return cnt
    
    
#     0 3
#     1 2
#     2 1 3
#     3 0 2