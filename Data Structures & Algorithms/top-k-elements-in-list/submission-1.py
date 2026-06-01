class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)

        arr = list(sorted(list(d.items()), key = lambda x: -x[1]))
        
        res = []

        for i in range(k):
            res.append(arr[i][0])
        return res
