# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# recursive
# class Solution(object):
#     def reverse(self, head):
#         """
#         input: ListNode head
#         return: ListNode
#         """
#         # write your solution here
#         if not head or not head.next:
#             return head
#
#         newHead = self.reverse(head.next)
#         head.next.next = head
#         head.next = None
#         return newHead

class Solution(object):
    def reverse(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        if not head or not head.next:
            return head

        cur = head
        prev = None
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev


testArray = [1,2,3,4,5,6]
head = ListNode(testArray[0])
cur = head
for a in testArray[1:]:
    cur.next = ListNode(a)
    cur = cur.next

newHead = Solution().reverse(head)
print(newHead)