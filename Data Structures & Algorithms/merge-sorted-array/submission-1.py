class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        i, j, k = m - 1, n-1, len(nums1) - 1

        while i >= 0 and j>= 0:
            if nums1[i] >= nums2[j]:
                swap(nums1, i, k)
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        while i >= 0:
            swap(nums1, i, k)
            i -= 1
            k -= 1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        