class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        leng=len(nums)
        i=0
        for j in range(leng):
            if nums[i]==val:
                nums.pop(i)
                i=i-1
                leng=len(nums)
            i=i+1    
            #nums.append(k*val)
        return leng
