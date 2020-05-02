#https://leetcode.com/problems/lucky-numbers-in-a-matrix/
class Solution:
    #O(mn) complexity)
    def luckyNumbers(self, matrix):
        minrow = [min(row) for row in matrix]
        maxcol = [max([matrix[row][col] for row in range(len(matrix))])for col in range(len(matrix[0]))]
        return [item for item in minrow if item in maxcol]
