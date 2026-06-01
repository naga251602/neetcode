class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for i in strs:
            temp = i
            key = ''.join(sorted(i))
            hm[key].append(temp)

        return list(hm.values())
