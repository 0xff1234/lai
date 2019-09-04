class Solution(object):
    def quickSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if not array or len(array) == 0:
            return array

        return self.qs(array, 0, len(array) - 1)

    def qs(self, array, left, right):
        pivot_position = self.partition(array, left, right)
        if left < pivot_position:
            self.qs(array, left, pivot_position - 1)

        if pivot_position < right:
            self.qs(array, pivot_position + 1, right)

        return array

    def partition(self, array, left, right):
        pivotIdx = self.selectPivot(left, right)
        pivot = array[pivotIdx]
        self.swap(array, pivotIdx, right)
        right -= 1
        oriLeft = left
        oriRight = right
        while left <= right :
            if left <= oriRight and array[left] < pivot :
                left += 1
            elif right >= oriLeft and array[right] > pivot:
                right -= 1
            else:
                self.swap(array,left, right)
                left +=1
                right -=1

        self.swap(array, left, pivotIdx)
        return left



    def selectPivot(self,left, right):
        return right

    def swap(self, array, left, right):
        temp = array[left]
        array[left] = array[right]
        array[right] = temp

# testArray = [8,7,6,5,4,3,2,1]
testArray = [8,7,4,7,6,5,4,4,3,2,7,1]

solution = Solution()
print(solution.quickSort(testArray))