#define pb push_back
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        vector<int> right(nums.size(), nums[nums.size() - 1]), res;

        for (int i = nums.size() - 2; i >= 0; i --) {
            right[i] = right[i+1] * nums[i];
        }

        int p = 1;

        for(int i = 0; i < nums.size(); i ++) {
            if (i == 0) res.pb(right[i+1]);
            else if (i == nums.size() - 1) res.pb(p);
            else res.pb(p * right[i + 1]);
            p *= nums[i];
        }

        return res;
    }
};
