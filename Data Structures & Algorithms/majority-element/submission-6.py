class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele, count = nums[0], 1

        for i in nums:
            if ele == i: count += 1
            else:
                if count <= 0: ele, count = i, 1
                else: count -= 1
        
        return ele