class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rev(nums, st, en):
            while st < en:
                nums[st], nums[en] = nums[en], nums[st]
                st += 1
                en -= 1
        k = k%len(nums)
        rev(nums, 0, len(nums) - k - 1)
        rev(nums, len(nums) - k, len(nums) - 1)
        rev(nums, 0, len(nums)-1)
        