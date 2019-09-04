

class Solution(object):
    def permutations(self, set):
        """
        input: string set
        return: string[]
        """
        # write your solution here
        if not set or len(set) == 0:
            return [set]

        solutions = []

        self.doPermutation(list(set), 0, solutions)
        return solutions

    def doPermutation(self, set:list, index, solutions):
        if index == len(set):
            solutions.append(''.join(set))
            return

        for i in range(index, len(set)):
            set[index],set[i] = set[i], set[index]
            self.doPermutation(set, index + 1, solutions)
            set[index],set[i] = set[i], set[index]




so = Solution()
print(so.permutations('abc'))
# print(so.permutations(''))
# print(so.permutations(None))