class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (m == nums1.size()) return;
        
        int i = m-1, j = nums2.size() - 1;
        int k = nums1.size() - 1;

        while (i >= 0 && j >= 0){
            if (nums1[i] > nums2[j]) swap(nums1[i --], nums1[k --]);
            else swap(nums1[k --], nums2[j --]);
        }

        while (i >= 0) {
            swap(nums1[i --], nums1[k --]);
        }

        while (j >= 0) {
            swap(nums1[k --], nums2[j --]);
        }
    }
};