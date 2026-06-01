class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, l, m, h):
            p = m - l + 1
            q = h - m

            left = [0] * p
            right = [0] * q

            for i in range(p):
                left[i] = nums[l+i]
            for j in range(q):
                right[j] = nums[m+j+1]
            
            k, i, j = l, 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
                
        def merge_sort(nums, l, h):
            if l < h:
                m = l + (h - l) // 2
                merge_sort(nums, l, m)
                merge_sort(nums, m+1, h)
                merge(nums, l, m, h)
        
        merge_sort(nums, 0, len(nums) - 1)
        return nums

        