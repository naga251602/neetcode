class Solution {
public:
    void sortColors(vector<int>& nums) {
        int st = -1, en = nums.size(), i = 0;

        while (i != en) {
            if (nums[i] == 0 && i != st) swap(nums[i], nums[++ st]);
            else if (nums[i] == 2) swap(nums[i], nums[-- en]);
            else i += 1;
        }
    }
};