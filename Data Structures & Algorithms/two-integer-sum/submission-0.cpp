class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;

        for (int i = 0; i < nums.size(); i ++) {
            int key = target - nums[i];
            // finding if subtraction exists 
            // always m[num[i]] < i cause its already seen!!
            if (m.find(nums[i]) != m.end()) return {m[nums[i]], i};
            // just add it!
            else m.insert({key, i});
        }

        return {};
    }
};
