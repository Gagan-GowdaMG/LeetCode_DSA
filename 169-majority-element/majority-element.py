class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        con=Counter(nums)
        return con.most_common(1)[0][0]
        