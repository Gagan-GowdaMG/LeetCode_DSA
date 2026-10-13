class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)
        if target not in nums:
            nums.append(target)
            nums.sort()
        print(nums)    
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
