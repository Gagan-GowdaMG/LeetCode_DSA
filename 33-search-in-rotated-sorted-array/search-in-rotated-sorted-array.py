class Solution:
    def search(self, nums: list[int], target: int) -> int:
        temp=[]
        i=0
        mid=len(nums)//2
        last=len(nums)-mid
        while i<mid:
            temp.append(nums[i])
            i=i+1
        while len(nums)<mid:
            j=0
            nums.pop(j)
        #print("temp",temp)    
        #print("nums",nums)    
        nums.extend(temp)
        #print(nums)
        if target in nums:
            return nums.index(target)
        else:
            return -1        


        