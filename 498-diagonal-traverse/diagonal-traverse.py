class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        row=len(mat)
        col=len(mat[0])
        result=[]

        for i in range(row+col-1):
            if i%2==0:
                r=min(i,row-1)
                c=i-r

                while r>=0 and c<col:
                    result.append(mat[r][c])
                    r-=1
                    c+=1
            else:
                c=min(i,col-1)
                r=i-c

                while c>=0 and r<row:
                    result.append(mat[r][c])
                    r+=1
                    c-=1
        return result









                


        