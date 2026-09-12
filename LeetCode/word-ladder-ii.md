# 🟠 word-ladder-ii — Word Ladder II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/word-ladder-ii/) &nbsp;|&nbsp; **Solved:** 2026-02-28

---

## 📝 Summary

Given two words and a dictionary, find all shortest transformation sequences from the start word to the end word.

## 🔍 Key Observation

The solution uses a breadth-first search (BFS) to explore all possible transformations, maintaining a parent graph to reconstruct paths.

## ⚙️ Algorithm

1. Build a graph where each word is a node and edges connect words that differ by exactly one character.
2. Use BFS to explore the graph starting from the beginWord. Keep track of visited words and the level of each word.
3. For each word at the current level, generate all possible transformations by changing one character at a time.
4. If a transformation matches the endWord, mark it as found and backtrack to reconstruct all paths from the endWord to the beginWord.
5. Collect all valid paths and return them.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m^2) where n is the number of words and m is the length of the words.` | `O(n * m^2) for the graph and visited set.` |

## 🏷️ Tags

`bfs` `graph` `word ladder`

<details>
<summary>💻 View solution</summary>

```python
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
```

</details>
