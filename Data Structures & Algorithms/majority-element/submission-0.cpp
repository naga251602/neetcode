class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> um;

        for (int i = 0; i < nums.size(); i ++) {
            um[nums[i]] ++;
        }

        vector<pair<int, int>> arr(um.begin(), um.end());

        sort(arr.begin(), arr.end(), [&](pair<int, int> a, pair<int, int> b) {
            return a.second > b.second;
        });

        return arr[0].first;
    }
};