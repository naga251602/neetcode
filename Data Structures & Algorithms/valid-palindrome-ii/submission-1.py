class Solution:
    def isPalin(self, s:str, st: int, en: int) -> bool:
        while st < en:
            if s[st] != s[en]: return False
            st += 1
            en -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        st, en = 0, len(s) - 1

        while st < en:
            if s[st] != s[en]: return self.isPalin(s, st+1, en) or self.isPalin(s, st, en-1)
            st += 1
            en -= 1
        return True
        