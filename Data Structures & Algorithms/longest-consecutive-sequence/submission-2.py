class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)

        s = set(nums)
        max_len = 0

        for i in s:
            if i-1 not in s:
                l = 1
                temp = i

                while temp + 1 in s:
                    l += 1
                    temp += 1
                max_len = max(l, max_len)

        return max_len
                    
