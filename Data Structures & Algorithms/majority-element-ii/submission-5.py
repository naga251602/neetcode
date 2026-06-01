class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2: return nums
        ele_1 = nums[0]
        ele_2 = nums[1]
        cnt_1 = 0
        cnt_2 = 0

        for i in range(0, len(nums)):
            if nums[i] == ele_1: cnt_1 += 1
            elif nums[i] == ele_2: cnt_2 += 1
            else:
                if cnt_1 == 0:
                    ele_1 = nums[i]
                    cnt_1 = 1
                elif cnt_2 == 0:
                    ele_2 = nums[i]
                    cnt_2 = 1
                else:
                    cnt_1 -= 1
                    cnt_2 -= 1
        
        cnt_1, cnt_2 = 0, 0
        for i in nums:
            if i == ele_1: cnt_1 += 1
            elif i == ele_2: cnt_2 += 1

        res = []
        if cnt_1 > len(nums) // 3: res.append(ele_1)
        if cnt_2 > len(nums) // 3: res.append(ele_2)  

        return res        