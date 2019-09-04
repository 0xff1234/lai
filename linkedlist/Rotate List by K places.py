class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.val) + ' -> ' + str(self.next)
        else:
            return str(self.val) + ' -> ' + 'None'



class Solution(object):
    def rotateKplace(self, head, n):
        """
        input: ListNode head, int n
        return: ListNode
        """
        # write your solution here
        if head == None or head.next == None or n == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cnt = 0
        total = self.doRotate(dummy, head , cnt + 1, n)
        return dummy.next

    def doRotate(self, dummy, head, cnt, k):
        if head == None:
            return cnt - 1
        total = self.doRotate(dummy, head.next, cnt + 1, k)
        k = k % total
        if 0 < total - cnt <= k:
            head.next.next = dummy.next
            dummy.next = head.next
            head.next = None

        # print(total)
        # print(cnt)
        # print(head)

        return total




testArray = [1,2]
head = ListNode(testArray[0])
cur = head
for a in testArray[1:]:
    cur.next = ListNode(a)
    cur = cur.next
print(head)

newHead = Solution().rotateKplace(head,6)
print(newHead)