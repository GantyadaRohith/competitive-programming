class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        w=sentence.split()
        for i,j in enumerate(w):
            if j.startswith(searchWord):
                return i+1
        return -1
