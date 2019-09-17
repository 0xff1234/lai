class Solution(object):
    def dedup(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if len(array) == 1:
            return array
        slow = 0
        fast = 1
        while fast < len(array):
            if array[slow] != array[fast] or slow < 1 or array[slow - 1] != array[fast]:
                slow += 1
                array[slow] = array[fast]
            fast += 1
        return array[0:slow + 1]


so = Solution()

arr = [1,1,1]
print(so.dedup(arr))