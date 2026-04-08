class Solution {
public:
    static void merge(vector<int>& nums, int l, int m, int h) {
        int p = m - l + 1;
        int q = h - m;

        vector<int> left(p, 0);
        vector<int> right(q, 0);

        for (int i = 0; i < p; i ++) {
            left[i] = nums[l + i];
        }

        for (int j = 0; j < q; j ++) {
            right[j] = nums[m + j + 1];
        }

        int i = 0, j = 0, k = l;

        while (i < p and j < q) {
            if (left[i] <= right[j]) nums[k ++] = left[i ++];
            else nums[k ++] = right[j ++];
        }

        while (i < p) { nums[k ++] = left[i ++]; }

        while (j < q) { nums[k ++] = right[j ++]; }
    }
    static void mergeSort(vector<int>& nums, int l, int h) {
        if (l < h) {
            int m = l + (h - l) / 2;

            mergeSort(nums, l, m);
            mergeSort(nums, m+1, h);
            merge(nums, l, m, h);
        }
    }
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size() - 1);
        return nums;
    }
};