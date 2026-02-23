class Solution(object):
    def rotate(self, matrix):
        "nothing"
        for  i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
            
        for i in range(len(matrix)):
            matrix[i].reverse()

        return matrix

  