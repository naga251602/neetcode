class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [0] * len(nums)
        r[-1] = nums[-1]
        
        for i in range(len(nums)-2, -1, -1):
            r[i] = nums[i] * r[i+1]
        
        res = []
        l = 1

        for i in range(len(nums)):
            if i == 0: res.append(r[i+1])
            elif i == len(nums) - 1: res.append(l)
            else:
                res.append(l * r[i+1])
            l *= nums[i]
            
        return res