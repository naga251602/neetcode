class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, i, r = -1, 0, len(nums)

        while i < len(nums) and i != r:
            if nums[i] == 0 and i != l:
                nums[i], nums[l+1] = nums[l+1], nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r-1] = nums[r-1], nums[i]
                r -= 1
            else:
                i += 1
        