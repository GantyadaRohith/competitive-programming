class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ch = {
            1:'qwertyuiop',
            2:'asdfghjkl',
            3:'zxcvbnm'
        }
        def find(word):
            for i,row in ch.items():
                if word[0].lower() in row:
                    return i
        out = []
        for i in words:
            temp = find(i)
            f = 1
            for j in range(1,len(i)):
                if i[j].lower() not in ch[temp]:
                    f = 0
                    break
            if f:
                out.append(i)
        return out 
