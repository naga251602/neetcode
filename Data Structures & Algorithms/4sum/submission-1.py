class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]: continue
                st = j + 1
                en = len(nums) - 1

                while st < en:
                    t = nums[i] + nums[st] + nums[en] + nums[j]
                    if t == target:
                        res.append([nums[st], nums[i], nums[j], nums[en]])
                        st += 1
                        en -= 1
                        
                        while st < en and nums[st] == nums[st-1]: st += 1
                        while st < en and nums[en] == nums[en+1]: en -= 1
                    
                    elif t < target: st += 1
                    else: en -= 1
            
        return res