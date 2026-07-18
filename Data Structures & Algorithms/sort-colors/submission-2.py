class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]

        for i in nums:
            counts[i] += 1
                
        counter = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[counter] = i
                counter += 1
        
        