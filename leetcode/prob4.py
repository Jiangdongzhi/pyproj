import sys
import os
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        iter1 = 0
        iter2 = 0
        current = 0
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1 + len2 + 1
        prev = 0
        recent = 0
        res = 0
        
        while (iter1 < len1 and iter2 < len2):
            if (nums1[iter1] <= nums2[iter2]):
                prev = recent
                recent = nums1[iter1]
                iter1 += 1
                current += 1
            if (current == length / 2):
                res = recent
                return res
            elif (current > length / 2):
                res = (recent + prev) / 2
                return res
            if (iter1 < len1 and nums1[iter1] >= nums2[iter2]):
                prev = recent
                recent = nums2[iter2]
                iter2 += 1
                current += 1
            if (current == length / 2):
                res = recent
                return res
            elif (current > length / 2):
                res = (recent + prev) / 2
                return res
        while (iter1 < len1):
            prev = recent
            recent = nums1[iter1]
            iter1 += 1
            current += 1
            if (current == length / 2):
                res = recent
                return res
            elif (current > length / 2):
                res = (recent + prev) / 2
                return res
        while (iter2 < len2):
            prev = recent
            recent = nums2[iter2]
            iter2 += 1
            current += 1
            if (current == length / 2):
                res = recent
                return res
            elif (current > length / 2):
                res = (recent + prev) / 2
                return res

if __name__ == '__main__':
    argv = sys.argv
    sol = Solution()

    print (sol.findMedianSortedArrays([1, 1, 3, 3], [1, 1, 3, 3]))


