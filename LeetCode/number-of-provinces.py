class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #dfs
        n = len(isConnected)
        cnt = 0
        va = [False]*n
        def dfs(graph,city):
            for nei in range(n):
                if graph[city][nei] == 1 and not va[nei] :
                    va[nei] = True
                    dfs(graph,nei)
        for i in range(n):
            if not va[i]:
                va[i] = True
                dfs(isConnected,i)
                cnt+=1
        return cnt