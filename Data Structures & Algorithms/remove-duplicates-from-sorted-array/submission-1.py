class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        l = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[l]: 
                swap(nums, i, l+1)
                l += 1
                
        return l+1