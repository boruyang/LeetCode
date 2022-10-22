// 0001. Two Sum //

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        vector<pair<int, int>> pairs(nums.size());
        for (int i = 0; i < nums.size(); ++i)
            pairs[i] = make_pair(nums[i], i);
        sort(pairs.begin(), pairs.end());
        int head = 0; int tail = nums.size() - 1;
        while (head < tail)
        {
            int current = pairs[head].first + pairs[tail].first;
            if (current == target)
                return {pairs[head].second, pairs[tail].second};
            else if (current < target)
                head += 1;
            else
                tail -= 1;
        }
        return {};
    }
};

int main()
{   
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> answer = solution.twoSum(nums, target);
    for (int i = 0; i < answer.size(); ++i)
        cout << answer[i] << endl;
    return 0;
}