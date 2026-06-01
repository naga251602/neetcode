class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: List[int]) -> None:
        st, en = -1, len(nums)
        i = 0
        while i != en and i < len(nums):
            if nums[i] == 0 and i != st:
                self.swap(nums, i, st+1)
                st += 1
            elif nums[i] == 2:
                self.swap(nums, i, en-1)
                en -= 1
            else: i += 1
        print(nums)
                


        