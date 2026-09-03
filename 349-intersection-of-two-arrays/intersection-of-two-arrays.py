class Solution(object):
    def intersection(self, nums1, nums2):
        
        nums1=set(nums1)

        ans=set()


        for i in nums2:
            if i in nums1:
                ans.add(i)
        return list(ans)




 





        # count=[]
        # u=[]
        # freq={}

        # for i in nums1:
        #     if i  in nums2:
        #         count.append(i)



        # for i in count:
        #     freq[i]=freq.get(i,0)+1


        # for i in freq:
        #     if freq[i]>=1:
        #         u.append(i)


            
  


        # return u