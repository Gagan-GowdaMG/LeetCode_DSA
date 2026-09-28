class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        j=1
        nums=sorted(nums)
        print(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                continue 
            if j==nums[i]:
                j=j+1
        return j             
        