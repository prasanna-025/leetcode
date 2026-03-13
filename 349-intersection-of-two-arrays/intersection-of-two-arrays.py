class Solution(object):
    def intersection(self, nums1, nums2):
        count=[]
        i=0
        while i<len(nums1):
            target=nums1[i]
            l=0
            while l<len(nums2):
                if target==nums2[l] and target not in count:
                    count.append(target)
                l+=1
            i+=1
        return count