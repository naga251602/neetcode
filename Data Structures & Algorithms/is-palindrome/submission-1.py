class Solution:
    def isPalindrome(self, s: str) -> bool:
        st, en = 0, len(s) - 1

        while st < en:
            if s[st].isalnum() and s[en].isalnum():
                if s[st].lower() != s[en].lower(): return False
                st += 1
                en -= 1
            else:
                if not s[st].isalnum(): st += 1
                if not s[en].isalnum(): en -= 1

        return True