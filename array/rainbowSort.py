class Solution(object):
    def rainbowSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if not array or len(array) == 0:
            return array

        i = 0
        j = 0
        k = len(array) - 1
        while j <= k :
            if array[j]  == -1 :
                array[i], array[j] = array[j], array[i]
                i += 1
                j += 1
            elif array[j] == 0:
                j +=1
            else:
                array[j],array[k] = array[k], array[j]
                k -= 1
        return array



testArrays = [[1,1,0,-1,0,1,-1]]
solution = Solution()
for testCase in testArrays:
    print(solution.rainbowSort(testCase))