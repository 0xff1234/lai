# https://app.laicode.io/app/problem/40

from linkedlist.common import ListNode
from linkedlist.common import array2linkedList


# L1 = 1 -> 4 -> 6 -> null, L2 = 2 -> 5 -> null, merge L1 and L2 to 1 -> 2 -> 4 -> 5 -> 6 -> null
# L1 = null, L2 = 1 -> 2 -> null, merge L1 and L2 to 1 -> 2 -> null
# L1 = null, L2 = null, merge L1 and L2 to null


class Solution(object):
    def merge(self, one, two):
        """
        input: ListNode one, ListNode two
        return: ListNode
        """
        # write your solution here
        if not one:
            return two

        if not two:
            return one

        if one.val < two.val:
            newHead = one
            one = one.next
        else:
            newHead = two
            two = two.next
        cur = newHead
        while one != None and two != None :
            if one.val < two.val:
                cur.next = one
                one = one.next
            else:
                cur.next = two
                two = two.next
            cur = cur.next
        if one == None:
            cur.next = two
        else:
            cur.next = one
        return newHead




testArray = [[0,5,5,5,8,10],[2,3,4,4,5,7]]
head1 = array2linkedList(testArray[0])
head2 = array2linkedList(testArray[1])

newHead = Solution().merge(head1, head2)
print(newHead)