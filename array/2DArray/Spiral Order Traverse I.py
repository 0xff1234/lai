
class Solution(object):
    def spiral(self, matrix):
        """
        input: int[][] matrix
        return: Integer[]
        """
        # write your solution here
        m = len(matrix)
        n = len (matrix[0])
        res = []
        self.doSpiral(matrix, 0, 0, m, n , res)
        return res

    def doSpiral(self,matrix, p,q, m ,n,res:list):
        if m == 0 or n == 0:
            return
        elif m == 1:
            for i in range(q, q + n):
                res.append(matrix[p][i])
            return
        elif n == 1:
            for i in range (p, p + m):
                res.append(matrix[i][q])
            return
        for i in range(q , q + n - 1):
            res.append(matrix[p][i])
        for i in range(p , p + m - 1):
            res.append(matrix[i][ q + n - 1])
        for i in range(q + n - 1 , q, -1):
            res.append(matrix[p + m - 1][i])
        for i in range( p + m - 1 , p, -1):
            res.append(matrix[i][q])

        return self.doSpiral(matrix, p + 1, q + 1, m - 2, n - 2, res)




# matrix = [[[-85,56,37,48],[-25,-78,-29,62],[18,-60,-74,-84],[90,44,5,1]]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1, 2, 3, 4]]
so = Solution()
print(so.spiral(matrix))