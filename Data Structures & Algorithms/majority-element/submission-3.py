class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele, count = nums[0], 1

        for i in range(1, len(nums)):
            if nums[i] == ele: count += 1
            else:
                if count == 0:
                    ele, count = nums[i], 1
                else:
                    count -= 1

        return ele