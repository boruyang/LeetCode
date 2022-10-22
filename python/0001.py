### 0001. Two Sum ###

from typing import List

class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        seen_num = dict()
        for i, num in enumerate(nums):
            if target - num in seen_num:
                return [seen_num[target - num], i]
            elif num not in seen_num:
                seen_num[num] = i

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
