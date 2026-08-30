class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        w=len(mat)
        n=len(mat[0])

        result=[]


        for i in range(w+n-1):
            if i%2==0:
                r=min(i,w-1)
                c=i-r
                while r>=0 and c<n:
                    result.append(mat[r][c])
                    r-=1
                    c+=1
            else:
                c=min(i,n-1)
                r=i-c
                while c>=0 and r<w:
                    result.append(mat[r][c])
                    r+=1
                    c-=1

        return result




                


        