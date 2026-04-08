#define pb push_back
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> arr(nums.begin(), nums.end());
        
        for (int i: nums) { arr.pb(i); }
        
        return arr;
    }
};