class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False

        hm = [0] * 26
        
        for i in range(len(s)):
            hm[ord(s[i]) - 97] += 1;
            hm[ord(t[i]) - 97] -= 1;
        
        for i in range(len(hm)):
            if hm[i] != 0: return False
        
        return True