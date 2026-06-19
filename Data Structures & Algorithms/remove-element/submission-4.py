class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = -1

        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos+1], nums[i] = nums[i], nums[pos+1]
                pos += 1
        
        return pos+1