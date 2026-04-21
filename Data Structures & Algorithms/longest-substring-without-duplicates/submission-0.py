class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        
        l, r = 0, 1
        st = set()
        max_len = float('-inf')
        curr = 1
        st.add(s[l])

        while l < len(s) and r < len(s):
            if s[r] not in st:
                st.add(s[r])
                curr += 1
                r += 1
            else:
                print('pop:', s[l])
                st.remove(s[l])
                l += 1
                curr = r - l 
            print(st)
            max_len = max(curr, max_len)

        return max_len

