class Solution(object):
    def mergeSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        if len(array) == 0:
            return array

        return self.merge(array, 0, len(array) - 1)
        # write your solution here

    def merge(self, array, left ,right):

        if left == right:
            return [array[left]]

        middle = left + int((right - left)/2)
        leftSection = self.merge(array, left ,middle)
        rightSection = self.merge(array, middle + 1, right)
        return self.combine(leftSection, rightSection)

    def combine(self,leftSec, rightSec):
        arr = []
        i = j = 0
        leftLen = len(leftSec)
        rightLen = len(rightSec)
        while ( i < leftLen  and j <rightLen):
            if(leftSec[i] < rightSec[j]):
                arr.append(leftSec[i])
                i+=1
                if i >= leftLen:
                    arr.extend(rightSec[j:])
            else:
                arr.append(rightSec[j])
                j+=1
                if j >= rightLen:
                    arr.extend(leftSec[i:])


        return arr

testArray = [3,5,1,2,4,8]
solution = Solution()
print(solution.mergeSort(testArray))