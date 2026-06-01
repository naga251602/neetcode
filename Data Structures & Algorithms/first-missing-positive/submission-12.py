class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        mn, mx = float('inf'), float('-inf')
        while i < len(nums):
            mn = min(mn, nums[i])
            mx = max(mx, nums[i])
            pos = nums[i] - 1
            if nums[i] > 0 and pos < len(nums) and nums[pos] != nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else: i += 1

        i = 0

        while i < len(nums):
            if i+1 != nums[i]: break
            i += 1
        return i+1
