class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=len(nums)
        t=0
        for i in range(l):
            for j in range(0,l-i-1):
                if nums[j]>nums[j+1]:
                    t=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=t
        return (nums)
