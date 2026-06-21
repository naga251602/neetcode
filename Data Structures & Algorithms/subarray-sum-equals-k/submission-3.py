class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        res = 0
        s = dict({0: 1})

        for num in nums:
            c += num
            d = c - k

            res += s.get(d, 0)
            s[c] = 1 + s.get(c, 0)
        
        return res

