class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = -1

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[p + 1], nums[i] = nums[i], nums[p+1]
                p += 1
        
        return p+1