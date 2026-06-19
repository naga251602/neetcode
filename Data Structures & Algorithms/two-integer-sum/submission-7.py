class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()

        for i in range(len(nums)):
            key = target - nums[i]

            if nums[i] in m: return [m[nums[i]], i]
            m[key] = i
        
        return []
