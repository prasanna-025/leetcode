class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        k=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>=nums2[j]:
                k.append(nums2[j])
                j+=1

            else:
                k.append(nums1[i])
                i+=1
        while i<len(nums1):
            k.append(nums1[i])
            i+=1
        while j<len(nums2):
            k.append(nums2[j])
            j+=1
    
        r=len(k)-1
        m=(0+r)//2
        if len(k)%2==0:
            z=k[m]+k[m+1]
            p=(z/2.0)
            return p
        

        return k[m]

  