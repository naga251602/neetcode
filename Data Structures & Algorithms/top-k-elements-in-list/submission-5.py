class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        bucket = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            hm[i] = 1 + hm.get(i, 0)

        for key in hm:
            bucket[hm.get(key)].append(key)
        
        res = []

        for i in range(len(bucket) - 1, -1, -1):
            if k == 0: break
            if len(bucket[i]) != 0:
                for j in bucket[i]:
                    res.append(j)
                    k -= 1

        return res
        
