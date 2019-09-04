class Solution(object):
    def binarySearch(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        # write your solution here
        if not array or len(array) == 0:
            return -1

        return self.doBinarySearch(array, target, 0, len(array) - 1)
        return self.iterateBinarySearch(array, target)

    def doBinarySearch(self,array, target, left, right):
        # if(left == right):
        #     return -1

        middle = left + int((right - left) / 2)
        if(array[middle] == target):
            return middle
        elif( array[middle] < target and middle < right):
            return self.doBinarySearch(array, target, middle + 1,right)
        elif( array[middle] > target and middle > left):
            return self.doBinarySearch(array, target, left, middle - 1)

        return -1

    def iterateBinarySearch(self, array, target):
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = left + int((right - left) /2 )
            if array[mid] == target:
                return mid
            elif(array[mid] < target):
                if mid < right:
                    left = mid + 1
                else:
                    return -1
            else:
                if left < mid:
                    right = mid - 1
                else:
                    return -1


# array ,target =  [3,4,5,6,6,9,16],16
array ,target =  [3],4
so = Solution()
print(so.binarySearch(array,target))
