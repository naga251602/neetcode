class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if nums[i] > 0:
                pos = nums[i] - 1
                if pos < len(nums) and nums[i] != nums[pos]:
                    nums[i], nums[pos] = nums[pos], nums[i]
                else: i += 1
            else: i += 1
        
        for i in range(1, len(nums)+1):
            if i != nums[i-1]: return i
        return i+1