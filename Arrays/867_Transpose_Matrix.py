#leetcode 867

#Transpose Matrix

class Solution(object):
    def transpose(self, matrix):
        ans=[]
        for col in range(len(matrix[0])):
            temp=[]
            for row in range(len(matrix)):
                temp.append(matrix[row][col])
            ans.append(temp)
        return ans         

   
        