class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i, j in zip(matrix, matrix[1:]):
            if i[:len(i)-1] == j[1:]:
                continue
            else:
                return False
        return True