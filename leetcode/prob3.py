import sys
import os

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 1
        res = 1
        if (len(s) == 0):
            res = 0
        while (end < len(s)):
            loc = s[start:end].find(s[end])
            end += 1
            if (loc < 0):
                if (end - start > res):
                    res = end - start
            else:
                start += loc + 1
        return res

if __name__ == '__main__':
    argv = sys.argv
    sol = Solution()

    print (sol.lengthOfLongestSubstring("abdcfdefghjksadefcvsv"))
