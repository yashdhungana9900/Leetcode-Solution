#Leetcode 1572

#Matrix diagonal sum

class Solution(object):
    def diagonalSum(self, mat):
        total =0
        n=len(mat)
        for i in range(n):
        #primary diogonal
            total+=mat[i][i]
        #secondary diogonal
            total+=mat[i][n-1-i]
        #remove the middle element if counted twicw
        if n%2==1:
            total-=mat[n//2][n//2]

        return total 
