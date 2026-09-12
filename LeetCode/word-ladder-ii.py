from collections import defaultdict,deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        parent = defaultdict(list)#build the graph where we define which word is which words parent
        level = {beginWord}#
        visited = set()
        found = False
        while level and not found :
            next_level = set()
            for word in level:
                visited.add(word)

            for word in level:
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch == word[i]:
                            continue
                        new_word = word[:i] + ch + word[i+1:] 
                        if new_word in wordset and new_word not in visited:
                            if new_word == endWord:
                                found = True
                            next_level.add(new_word)
                            parent[new_word].append(word)
            level = next_level
        
        #build the dfs 
        result = []
        path = [endWord]
        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parents in parent[word]:
                path.append(parents)
                backtrack(parents)
                path.pop()
        if found:
            backtrack(endWord)
        return result