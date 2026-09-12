class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        for i in range(len(strs[0])):
            prefix = strs[0][:i+1]

            for s in strs:
                if s[:i+1] != prefix:
                    return strs[0][:i]

        return strs[0]