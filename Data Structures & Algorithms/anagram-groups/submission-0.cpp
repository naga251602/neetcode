#define pb push_back
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> arr;
        unordered_map<string, vector<string>> um;

        for(int i = 0; i < strs.size(); i ++) {
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            um[temp].pb(strs[i]);
        }

        for(pair<string, vector<string>> it: um) {
            vector<string> temp;
            for(int i = 0; i < it.second.size(); i ++) {
                temp.pb(it.second[i]);
            }
            arr.pb(temp);
        }
        
        return arr;
    }
};
