class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums[0]]

        num_1, num_2 = nums[0], nums[1]
        c1, c2 = 0, 0

        for i in range(len(nums)):
            if nums[i] == num_1: c1+=1
            elif nums[i] == num_2: c2+=1
            else:
                if c1 == 0:
                    num_1, c1 = nums[i], 1
                elif c2 == 0:
                    num_2, c2 = nums[i], 1
                else:
                    c1 -= 1
                    c2 -= 1
        
        c1, c2 = 0, 0
        for num in nums:
            if num == num_1: c1+=1
            elif num == num_2: c2+=1

        res = []
        if c1 > len(nums)//3: res.append(num_1)
        if c2 > len(nums)//3: res.append(num_2)

        return res