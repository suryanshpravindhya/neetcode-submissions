class Solution(object):
    def majorityElement(self, nums):
        count=0
        p=0
        mylist=list(set(nums))
        for k in mylist:
            s=nums.count(k)
            if count<s:
                count=s
                p=k
            else:
                continue
        return(p)
        