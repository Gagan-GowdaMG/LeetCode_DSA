class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        j=-1
        u=0
        for i in range(len(s)):
            if s[j]==" ":
                break
            else:
                j-=1
                u+=1
        return u        


        