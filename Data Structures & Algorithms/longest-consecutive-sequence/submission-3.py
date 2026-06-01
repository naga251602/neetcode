class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        s = set()

        for i in nums: s.add(i)
        mx_len = 1
        for i in nums:
            if i + 1 not in s:
                n = i
                l = 0
                while n in s:
                    n -= 1
                    l += 1
                mx_len = max(l, mx_len)
        return mx_len