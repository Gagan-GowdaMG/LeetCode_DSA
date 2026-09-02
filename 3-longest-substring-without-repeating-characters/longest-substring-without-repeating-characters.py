class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        temp=0
        for i in range(n):
            seen=set()
            for j in range(i,n):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    temp=max(temp,j-i+1)
        return temp

        