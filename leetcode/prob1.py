import sys
import re
import os

class Solution:
    def twoSum(self, nums, target):
        comps = []
        res = []

        for item in nums:
            comps.append(target - item)

        for i in range(len(nums)):
            for j in range(len(comps)):
                if (nums[i] == comps[j] and i != j and nums[i] < nums[j]):
                    res.append(i)
                    res.append(j)
                    break

        return res

if __name__ == '__main__':
    argv = sys.argv
    sol = Solution()

    output = sol.twoSum([1, 2, 3, 4], 6)

    print(output)

