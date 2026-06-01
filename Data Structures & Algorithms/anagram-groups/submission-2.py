class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for i in strs:
            counter = [0] * 26
            for k in i: counter[ord(k) - 97] += 1
            hm[tuple(counter)].append(i)

        return list(hm.values())
