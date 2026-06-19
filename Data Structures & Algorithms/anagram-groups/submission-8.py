class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for i in range(len(strs)):
            c = [0] * 26
            for s in strs[i]:
                c[ord(s) - 97] += 1
            hm[tuple(c)].append(strs[i])

        return list(hm.values())