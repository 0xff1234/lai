

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __str__(self):
    #     if self.next:
    #         return str(self.val) + ' -> ' + str(self.next)
    #     else:
    #         return str(self.val) + ' -> ' + 'None'


def array2linkedList(array):
    head = ListNode(array[0])
    cur = head
    for a in array[1:]:
        cur.next = ListNode(a)
        cur = cur.next
    return head