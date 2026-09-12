class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 and strs[-1] == '':
            return [strs]
        out = defaultdict(list)
        for i in range(len(strs)):
            x = ''.join(sorted(strs[i]))
            out[x].append(strs[i])
        return list(out.values())