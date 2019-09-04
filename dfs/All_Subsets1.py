
class Solution(object):
    def subSets(self, set):
        """
        input : String set
        return : String[]
        """
        # write your solution here
        if not set or len(set) == 0:
            return [set]


        solutions = []
        self.doSubSet(set, 0, [],solutions )
        return solutions


    def doSubSet(self, set, level, answer, solutions):
        if level == len(set) :
            solutions.append( ''.join(answer))
            return

        answer.append(set[level])
        self.doSubSet(set, level + 1, answer, solutions)
        answer.pop()
        self.doSubSet(set, level + 1, answer, solutions)



so = Solution()
# print(so.subSets('abc'))
print(so.subSets(''))
print(so.subSets(None))