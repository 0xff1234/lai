# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def insert(self, head, value):
        """
        input: ListNode head, int value
        return: ListNode
        """
        # write your solution here
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        while cur != None and cur.next != None and cur.next.val < value:
            cur = cur.next

        if cur.next == None:
            cur.next = ListNode(value)
        else:
            temp = cur.next
            cur.next = ListNode(value)
            cur.next.next = temp

        return dummy.next
