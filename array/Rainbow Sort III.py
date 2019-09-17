class Solution(object):
    def rainbowSortIII(self, array, k):
        """
        input: int[] array, int k
        return: int[]
        """
        # write your solution here
        buckets = [0] * k
        for elem in array:
            buckets[elem - 1] += 1

        results = []
        for i in range(0 , k):
            results.extend([i + 1] * buckets[i])

        return results

so = Solution()
array = [2, 3, 3, 1, 1]
print(so.rainbowSortIII(array,3))