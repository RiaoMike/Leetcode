/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int len = nums.size();
        if (len < 4) return {};
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int i = 0; i < len - 3; ++i) {
            for (int j = i + 1; j < len - 2; ++j) {
                int left = j + 1;
                int right = len - 1;
                while (left < right) {
                    // 这里添加0.0用于将int转化为double， 防止整数溢出
                    double tmpSum = 0.0 + nums[i] + nums[j] + nums[left] + nums[right];
                    if (tmpSum == target) {
                        // update j position
                        result.push_back({nums[i], nums[j], nums[left], nums[right]});
                        left++;
                        while (nums[left] == nums[left - 1] && left < right) left++;
                        right--;
                        while (nums[right] == nums[right + 1] && right > left) right--;
                    }
                    else if (tmpSum < target) {
                        left++;
                        while (nums[left] == nums[left - 1] && left < right) left++;
                    }
                    else {
                        right--;
                        while (nums[right] == nums[right + 1] && right > left) right--;
                    }
                }
                // j < len - 1 目的是使j + 1下标不越界， j的范围会在for循环中进行判断
                // 找到最后一个连续相同的元素
                while (j < len - 1 && nums[j] == nums[j + 1]) j++;
            }
            // 这里的while和前面的while一样，为了防止重复，跳过重复的元素
            while (i < len - 1 && nums[i] == nums[i + 1]) i++;
        }
        if (result.empty()) return {};
        else return result;
    }
};
// @lc code=end