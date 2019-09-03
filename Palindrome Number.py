class Solution(object):
    def isPalindrome(self, x):
        stringx = str(x)
        li = []
        new = []
        for i in stringx:
            li.append(i)
            new.append(i)
        new.reverse()
        if new == li:
            return True
        else:
            return False
