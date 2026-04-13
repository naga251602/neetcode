class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int i = 0;
        
        while (i < nums.size()) {
            int pos = nums[i] - 1;
            if (nums[i] > 0 && nums[i] <= (int)nums.size() && nums[i] != nums[pos]) swap(nums[i], nums[pos]);
            else i ++;
        }

        i = 0;

        while(i < nums.size()) {
            if (i+1 != nums[i]) break;
            i ++;
        }

        return i + 1;
    }
};