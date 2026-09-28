class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        leng=len(nums)

        if leng==0:
            return 0
        k=0

        for i in range(1,leng):  
            if nums[k]!=nums[i]:
                k=k+1
                nums[k] = nums[i]
                #k=k+1
        return k+1         


        