import sys
import re
import os
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = []
        res : List[int] = []

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

