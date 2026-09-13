class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)
        if x<0:
            c=(a[:0:-1])
            c=int(c)
            if -2**31<c>(2**31)-1 :
                return 0
            else:
                return c*-1
        else:
            c=a[::-1]
            c=int(c)
            if -2**31<c>(2**31)-1 :
                return 0
            else:
                return c
