class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()

        for i in range(len(nums)):
            if nums[i] in hm: return [hm[nums[i]], i]
            hm[target - nums[i]] =  i
        
