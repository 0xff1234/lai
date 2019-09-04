from linkedlist.common import ListNode
from linkedlist.common import array2linkedList



#https://app.laicode.io/app/problem/35

class Solution(object):
    def reverseInPairs(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        if not head or not head.next:
            return head

        nextHead = self.reverseInPairs(head.next.next)
        newHead = head.next
        newHead.next = head
        head.next = nextHead
        return newHead


testArray = [5,4,3,2,1,0]
head = array2linkedList(testArray)

newHead = Solution().reverseInPairs(head)
print(newHead)