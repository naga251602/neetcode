class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int i = 0;
        
        while (i < nums.size()) {
            if (nums[i] > 0) {
                int idx = nums[i] - 1;
                if (idx <= nums.size() - 1 && nums[i] != nums[idx]) swap(nums[i], nums[idx]);
                else i ++;
            } else {
                i ++;
            }
        }

        i = 0;

        while (i < nums.size()) {
            if(i+1 != nums[i]) break;
            i ++;
        }

        return i + 1;
    }
};