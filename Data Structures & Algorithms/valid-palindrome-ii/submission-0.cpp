class Solution {
public:
    static bool isPalindrome(string &s,int st, int en) {
        while (st < en) {
            if (s[st ++] != s[en --]) return false;
        }

        return true;
    }
    bool validPalindrome(string s) {
        int st = 0, en = s.size() - 1;

        while (st < en) {
            if (s[st] != s[en]) return isPalindrome(s, st+1, en) || isPalindrome(s, st, en - 1);
            st ++;
            en --;
        }
        return true;
    }
};