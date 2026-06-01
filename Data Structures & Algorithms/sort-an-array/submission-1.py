def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

class Solution:
    def merge(self, nums, l, m, h):
        p = m - l + 1
        q = h - m

        left = [0] * p
        right = [0] * q

        for i in range(p):
            left[i] = nums[l + i]
        
        for j in range(q):
            right[j] = nums[m + j + 1]
        
        i, j, k = 0, 0, l

        while i < p and j < q:
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < p:
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < q:
            nums[k] = right[j]
            j += 1
            k += 1

    def merge_sort(self, nums, l, h):
        if l < h:
            m = l + (h - l) // 2
            self.merge_sort(nums, l, m)
            self.merge_sort(nums, m+1, h)
            self.merge(nums, l, m, h)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums
        