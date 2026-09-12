class Solution {
public:
    int search(vector<int>& nums, int target) {
        int first = 0;
        int last = nums.size(); // Correctly get the vector size
        int mid = (first + last) / 2;

        while (first < last) {
            if (nums[mid] == target) {
                return mid; // Target found, return index
            } else {
                if (nums[mid] < target) {
                    first = mid + 1; // Search in the right half
                } else {
                    last = mid; // Search in the left half
                }
            }
            mid = (first + last) / 2; // Recalculate mid
        }
        return -1; // Target not found
    }
};