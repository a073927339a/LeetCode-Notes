class Solution(object):
    def sortArrayByParity(self, A):
        li = []
        for i in A:
            if i % 2 == 0:
               li.append(i)
        for i in A:
            if i % 2 == 1:
                li.append(i)
        return li
        