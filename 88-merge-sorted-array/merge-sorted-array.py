class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=0
        j=0
        x=[]
        while i<m and j<n:
                if nums1[i]<=nums2[j]:
                    x.append(nums1[i])
                    i=i+1
                else:
                    x.append(nums2[j])
                    j+=1
        while i<m:
            x.append(nums1[i])
            i+=1
        while j<n:
            x.append(nums2[j])
            j+=1
        
        for i in range(m+n):
            nums1[i]=x[i]

  

            

        