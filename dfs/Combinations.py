class Solution(object):
    def combine(self, n, k):
        """
        input: int n, int k
        return: int[][]
        """
        # write your solution here
        self.solutions = list()
        self.n = n
        self.k = k
        self.doCombine(0, [], 1)
        return list(self.solutions)

    def doCombine(self, level, answer, start):
        if level == self.k:
            self.solutions.append(answer.copy())
            return


        for i in range(start, self.n + 1):
            answer.append(i)
            self.doCombine(level + 1, answer, i + 1)
            answer.pop()





so = Solution()
print(so.combine(4,2))