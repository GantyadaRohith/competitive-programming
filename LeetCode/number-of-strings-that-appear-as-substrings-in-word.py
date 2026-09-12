class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        out = 0 
        for i in patterns:
            if i in word:
                out+=1
        return out