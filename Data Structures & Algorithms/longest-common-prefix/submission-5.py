class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = []
        i = 0
        n = min(len(strs[0]), len(strs[-1]))

        while i < n:
            if strs[0][i] != strs[-1][i]: break
            res.append(strs[0][i])
            i += 1
            
        return ''.join(res)