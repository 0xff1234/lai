class Solution(object):
    def sort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if not array or len(array) == 0:
            return array

        for i in range(1,len(array)):
            temp = array[i]
            j = i
            while(j > 0 and temp < array[j - 1]):
                array[j] = array[j - 1]
                j -= 1
            array[j] = temp
        return array


testArray = [-85,-28,-78,-57,-25,4,-93,62,77,-5,-25,-53,-37,-69,48,24,16,-63,67,95,2,-96,70,7,-49,3,-62,-67,-42,24,-33,-31,-12,96,-54,98,-5,21,-69,94,-20,-48,-50,32,-37,-51,-61,74,36,78,-85,36,45,50,17,-27,85,5,10,90,-17,-4,-57,-68,-74,36,-24,38,-60,-66,-40,37,-30,-14,98,-81,-44,29,-32,68,-19,-39,98,25,-3,46,-13,50,-57,-48]
solution = Solution()
print(solution.sort(testArray))