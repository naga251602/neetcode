class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            st = i + 1
            en = len(nums) - 1

            while st < en:
                t = nums[i] + nums[st] + nums[en] 
                if t == 0:
                    res.append([nums[st], nums[i], nums[en]])
                    st += 1
                    en -= 1
                    
                    while st < en and nums[st] == nums[st-1]: st += 1
                    while st < en and nums[en] == nums[en+1]: en -= 1
                
                elif t < 0: st += 1
                else: en -= 1
            
        return res