from linkedlist.common import ListNode
from linkedlist.common import array2linkedList


#https://app.laicode.io/app/problem/42
'''
Given a linked list and a target value T, partition it such that all nodes less than T are listed before the nodes larger than or equal to target value T. The original relative order of the nodes in each of the two partitions should be preserved.

Examples

L = 2 -> 4 -> 3 -> 5 -> 1 -> null, T = 3, is partitioned to 2 -> 1 -> 4 -> 3 -> 5 -> null
'''

class Solution(object):
    def partition(self, head, target):
        """
        input: ListNode head, int target
        return: ListNode
        """
        # write your solution here
        if not head or not head.next:
            return head


        smallHead = largeHead = None
        smallCur = largeCur = None
        cur = head
        while cur != None:
            next = cur.next
            cur.next = None
            if cur.val < target:
                if smallHead == None:
                    smallHead = cur
                    smallCur = cur
                else:
                    smallCur.next = cur
                    smallCur = smallCur.next
            else:
                if largeHead == None:
                    largeHead = cur
                    largeCur = cur
                else:
                    largeCur.next = cur
                    largeCur = largeCur.next
            cur = next
        if smallCur == None or smallHead == None:
            return largeHead
        smallCur.next = largeHead
        return smallHead



testArray = [2 , 4 , 3 , 5 , 1]
newHead = array2linkedList(testArray)
print(Solution().partition(newHead,3))