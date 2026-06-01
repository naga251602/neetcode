class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        r = [nums[-1]] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i+1] * nums[i]
        res = []

        for i in range(len(nums)):
            if i == 0: res.append(r[i+1])
            elif i == len(nums) - 1: res.append(l)
            else:
                res.append(l * r[i+1])
            l *= nums[i]
        
        return res