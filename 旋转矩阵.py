class Solution:
    def rotateMatrix(self, mat, n):
        resultmatrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                resultmatrix[j][n-i-1] = mat[i][j]
        return resultmatrix
# 原地tp，空间O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

# 原地tp，先水平翻转，再对角线翻转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
               matrix[i][j],matrix[n-i-1][j] = matrix[n-1-i][j],matrix[i][j]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix