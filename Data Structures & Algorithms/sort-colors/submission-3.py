class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        l, r = -1, len(nums)
        i = 0
        while i != r:
            if i != l and nums[i] == 0:
                swap(nums, i, l+1)
                l += 1
            elif nums[i] == 2:
                swap(nums, i, r-1)
                r -= 1
            else: i += 1
        
