class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(m,len(nums1)):
            nums1[i]=nums2[j]
            j=j+1
        for i in range(len(nums1)):
            for j in range(len(nums1)-i-1):
                if nums1[j]>nums1[j+1]:
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]   
        