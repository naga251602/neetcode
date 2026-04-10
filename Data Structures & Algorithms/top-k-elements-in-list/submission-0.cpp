class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hm;

        for (int i = 0; i < nums.size(); i ++) {
            hm[nums[i]] ++;
        }

        vector<int> res;
        vector<pair<int, int>> arr(hm.begin(), hm.end());

        sort(arr.begin(), arr.end(), [&](pair<int, int> a, pair<int, int> b) {
            return a.second > b.second;
        });

        int i = 0;

        for (pair<int, int> a: arr) {
            if (i == k ) break;
            res.push_back(a.first);
            i ++;
        }
        return res;
    }
};
