class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for index,i in enumerate(nums):
            difference=target-i
            if difference in s:
                return [s[difference],index]
            s[i]=index
        return []