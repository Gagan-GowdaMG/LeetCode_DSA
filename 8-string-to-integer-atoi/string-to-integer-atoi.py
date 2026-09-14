class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        i=0
        num=0
        num1=0
        if len(s)==0:
            s="0"
        if s[0]=="-":
            sign=-1
        else:
            sign=1
        print(sign)     
        if s[i]=="-"or s[i]=="+":
            i=i+1   
        while i<len(s) and s[i].isdigit():
            num=int(s[i])
            i=i+1
            num1=num1*(10)+num
            
        num1=num1*sign    
        if num1<(-2**31):
            num1=-2**31
        if num1>(2**31-1):
            num1=2**31-1
        return num1    



        




        
        