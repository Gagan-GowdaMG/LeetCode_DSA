class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            s=haystack.index(needle)
            return s
        else:
            return -1    
        