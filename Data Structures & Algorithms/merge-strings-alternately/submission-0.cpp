class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i = 0, j = 0, k = 0;
        string res;
        while (i < word1.length() && j< word2.length()) {
            if (k%2 == 0) res.push_back(word1[i ++]);
            else res.push_back(word2[j ++]);
            k ++;
        }

        while (i < word1.length()) {
            res.push_back(word1[i ++]);
        }

        while (j < word2.length()) {
            res.push_back(word2[j ++]);
        }

        return res;
    }
};