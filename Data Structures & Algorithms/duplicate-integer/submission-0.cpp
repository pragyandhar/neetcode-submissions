class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        int n = nums.size();
        int m = s.size();
        if (n == m) return false;
        else return true;
    }
};