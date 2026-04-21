class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        st = dict()

        for i in range(len(nums)):
            if nums[i] in st and i - st.get(nums[i]) <= k: return True
            st[nums[i]] = i
        
        return False