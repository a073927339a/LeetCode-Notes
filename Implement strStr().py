class Solution(object):
    def strStr(self, haystack, needle):
        str = ''
        if not needle:
            return 0
        elif needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i
        else:
            return -1
        
