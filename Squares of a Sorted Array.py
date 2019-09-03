class Solution(object):
    def sortedSquares(self, A):
        li = []
        a = 0
        for i in A:
            a = i*i
            li.append(a)
        li.sort()
        return li
        