class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();

        int max_len = 1;
        unordered_set<int> st;

        for (int i = 0; i < nums.size(); i ++) st.insert(nums[i]);

        for (int num: st) {
            if (st.find(num+1) != st.end()) {
                int curr_len = 0;
                int x = num;
                while (true) {
                    if (st.find(x) == st.end()) break;
                    curr_len ++;
                    x ++;
                }
                max_len = max(curr_len, max_len);
            }
            
           
        }
        return max_len;
    }
};
