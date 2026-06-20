class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = set(nums)
        mx = 0
        for i in l:
            count = 0
            while i in l:
                count += 1
                i -= 1
            mx = max(count, mx)
        return mx