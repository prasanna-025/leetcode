class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=matrix
        for i in range(len(m)):
            for j in range(len(m[0])):
                if  m[i][j]==0:
                    for x in range(len(m[0])):
                        if m[i][x]!=0:
                            m[i][x]=-99

                    for y in range(len(m)):
                        if m[y][j]!=0:
                            m[y][j]=-99

        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]==-99:
                    m[i][j]=0
                
    
     
        return m
                    
        