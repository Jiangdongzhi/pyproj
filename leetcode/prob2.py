import sys
import os

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        iter1 = l1
        iter2 = l2
        result = None
        temp = None
        carryon = 0
        
        while (iter1 != None or iter2 != None):
            tot = carryon
            if (iter1 != None):
                tot += iter1.val
                iter1 = iter1.next
            if (iter2 != None):
                tot += iter2.val
                iter2 = iter2.next
            node = ListNode(tot % 10)
            carryon = tot // 10
            if (result == None):
                result = node
            if (temp != None):
                temp.next = node
            temp = node
        if (carryon > 0):
            temp.next = ListNode(carryon)
        
        return result

if __name__ == '__main__':
    argv = sys.argv
    sol = Solution()

    arg1 = ListNode(5)
    arg1.next = ListNode(9)
    arg1.next.next = ListNode(9)
    arg1.next.next.next = ListNode(9)

    arg2 = ListNode(8)
#    arg2.next = ListNode(2)
#    arg2.next.next = ListNode(4)

    output = sol.addTwoNumbers(arg1, arg2)

    while (output != None):
        print(output.val)
        output = output.next
#    print(output)

