class Solution:
    

    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, l, m, h):
            p = m - l + 1
            q = h - m
            
            left = [0] * p
            right = [0] * q

            for i in range(p):
                left[i] = nums[l + i]
            
            for j in range(q):
                right[j] = nums[m + j + 1]
            
            k = l
            i, j = 0, 0

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
        def mergeSort(nums, l, h):
            if l < h:
                m = l + (h - l) // 2
                mergeSort(nums, l, m)
                mergeSort(nums, m + 1, h)
                merge(nums, l, m, h)
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums
        