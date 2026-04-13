class Solution {
public:
    bool isPalindrome(string s) {
        int st = 0, en = s.size() - 1;

        while (st < en) {
            if (isalnum(s[st]) && isalnum(s[en])) {
                if (tolower(s[st]) != tolower(s[en])) return false;
                st ++;
                en --;
            }

            while (!isalnum(s[st]) && st < en) st ++;
            while (!isalnum(s[en]) && en > st) en --;
        }

        return true;
    }
};
