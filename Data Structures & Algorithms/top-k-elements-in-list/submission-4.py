class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        f = [[] for i in range(len(nums)+1)]

        for ele, ct in c.items():
            f[ct].append(ele)

        res = []
        for i in range(len(f)-1, 0, -1):
            for j in f[i]:
                res.append(j)
                if len(res) == k: return res

        return []