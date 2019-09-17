

class Solution(object):
    def setZero(self, matrix):
        """
        input: int[][] matrix
        return: No need to return
        """
        # write your solution here
        if not matrix or len(matrix) == 0:
            return

        m = len(matrix)
        n = len(matrix[0])
        zero_elems = []
        for i in range(0,m):
            for j in range(0 , n):
                if matrix[i][j] == 0:
                    zero_elems.append([i,j])

        x_all_0 = [0] * m
        y_all_0 = [0] * n
        for elem in zero_elems:
            x = elem[0]
            if x_all_0[x] != 1:
                x_all_0[x] = 1
                for i in range(0,n):
                    matrix[x][i] = 0
            y = elem[1]
            if y_all_0[y] != 1:
                y_all_0[y] = 1
                for i in range(0,m):
                    matrix[i][y] = 0

Matrix =  [[1, 1, 1, 1, 0],
           [0, 1, 1, 0, 1],
           [1, 1, 1, 0, 1],
           [1, 1, 1, 1, 1]]
so = Solution()
so.setZero(Matrix)
print(Matrix)