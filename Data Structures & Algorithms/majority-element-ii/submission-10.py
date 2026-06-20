class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return [nums[0]]
        if len(nums) == 2: return nums

        ele1, ele2, count1, count2 = nums[0], nums[1], 0, 0

        for i in nums:
            if i == ele1: count1 += 1
            elif i == ele2: count2 += 1
            else:
                if count1 < 0:
                    ele1, count1 = i, 1
                elif count2 < 0:
                    ele2, count2 = i, 1
                else:
                    count1 -= 1
                    count2 -= 1
       
        n1, n2 = 0, 0
        for i in nums:
            if i == ele1: n1 += 1
            if i == ele2: n2 += 1
        
        res = []

        if n1 > (len(nums) // 3):
            res.append(ele1)
        if n2 > (len(nums) // 3) and ele2 != ele1:
            res.append(ele2)

        return res