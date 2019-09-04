

#https://app.laicode.io/app/problem/320
'''
Given a linked list and an sorted array of integers as the indices in the list. Delete all the nodes at the indices in the original list.

Examples

1 -> 2 -> 3 -> 4 -> NULL, indices = {0, 3, 5}, after deletion the list is 2 -> 3 -> NULL.

Assumptions

the given indices array is not null and it is guaranteed to contain non-negative integers sorted in ascending order.
'''
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNodes(self, head, indices):
        """
        input: ListNode head, int[] indices
        return: ListNode
        """
        # write your solution here
        if not head or len(indices) == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cnt = 0
        index = 0
        cur = dummy

        while cur != None and index < len(indices):
            if cnt == indices[index]:
                if  cur.next != None:
                    cur.next = cur.next.next
                    index += 1
            else:
                cur = cur.next
            cnt += 1


        return dummy.next

testArray = [1]
head = ListNode(testArray[0])
cur = head
for a in testArray[1:]:
    cur.next = ListNode(a)
    cur = cur.next

newHead = Solution().deleteNodes(head,[1,3,5])
print(newHead)