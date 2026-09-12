class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        values = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."] 
        mapping = {chr(97+i): values[i] for i in range(26)}
        out = []
        for word in words:
            s = ''
            for ch in word:
                s = s + mapping[ch]
            out.append(s)
        return len(set(out))
