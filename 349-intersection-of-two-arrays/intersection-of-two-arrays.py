class Solution(object):
    def intersection(self, nums1, nums2):

        nums2=set(nums2)
        ans=set()

        for i in nums1:
            if i in nums2:
                ans.add(i)
        return list(ans)




        # count=[]
        # u=[]
        # freq={}

        # for i in nums1:
        #     if i  in nums2:
        #         count.append(i)



        # for i in count:
        #     if i not in freq:
        #         freq[i]=1
        #     else:
        #         freq[i]+=1

        # for i in freq:
        #     if freq[i]>=1:
        #         u.append(i)


            
  


        # return u