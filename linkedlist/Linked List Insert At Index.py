# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def insert(self, head, index, value):
        """
        input: ListNode head, int index, int value
        return: ListNode
        """
        # write your solution here
        if index == 0:
            temp = head
            head = ListNode(value)
            head.next = temp
            return head

        cur = head
        cnt = 1
        while cnt < index and cur != None and cur.next != None:
            cur = cur.next
            cnt += 1

        if cnt == index:
            temp = cur.next
            cur.next = ListNode(value)
            cur.next.next = temp
        return head



class Solution(object):
    def insert(self, head, index, value):
        """
        input: ListNode head, int index, int value
        return: ListNode
        """
        # write your solution here
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        cnt = 0
        while cnt < index and cur != None and cur.next != None:
            cur = cur.next
            cnt += 1

        if cnt == index:
            temp = cur.next
            cur.next = ListNode(value)
            cur.next.next = temp
        return dummy.next