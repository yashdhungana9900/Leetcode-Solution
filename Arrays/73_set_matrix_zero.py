class Solution(object):
    def setZeroes(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        # Find all rows and columns containing 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set those rows to 0
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Set those columns to 0
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0