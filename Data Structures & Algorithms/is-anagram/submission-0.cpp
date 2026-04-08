class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        
        vector<int> h(26, 0);

        for (int i = 0; i < s.length(); i ++) {
            h[(int)(s[i]) - 97] ++;
            h[(int)(t[i]) - 97] --;
        }

        for(int i = 0; i < h.size(); i ++) {
            if (h[i] != 0) return false;
        }

        return true;
    }
};
