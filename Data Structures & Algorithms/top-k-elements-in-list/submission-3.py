class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        l1=[[] for i in range(len(nums)+1)]
        for n in nums:
            s[n]=1+s.get(n,0)
        for n,c in s.items():
            l1[c].append(n)
        l2=[]
        for j in range(len(l1)-1,0,-1):
            for n in l1[j]:
                l2.append(n)
            if len(l2)==k:
                break
                    
        return(l2)  
        