class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        out = {}
        cnt =0
        for i in range(len(mat)):
            cnt = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    cnt+=1
            out[i] = cnt
        maxi = max(list(out.values()))
        res = []
        for i,j in out.items():
            if j == maxi:
                return [int(i),int(j)]

