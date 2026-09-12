class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
            n = 34
            a = [[1],[1,1]]
            n-=2
            for i in range(1,n+1):
                a.append([1])
                for j in range(1,len(a[-2])):
                    a[-1].append(a[-2][j-1]+a[-2][j])
                a[-1].append(1)
            return a[rowIndex]      