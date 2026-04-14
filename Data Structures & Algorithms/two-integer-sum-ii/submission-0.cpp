class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int st = 0, en = numbers.size() - 1;

        while ( st < en) {
            int t = numbers[st] + numbers[en];

            if (t == target) break;
            else if(t < target) st ++;
            else en --;
        }

        return {st+1, en+1};
    }
};
