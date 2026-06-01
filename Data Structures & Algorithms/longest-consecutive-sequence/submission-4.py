class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        s = set(nums)
        max_len = 1
        for i in s:
            if i - 1 not in s:
                l = 0
                while i + l in s: l += 1
                max_len = max(max_len, l)
        return max_len