class Solution(object):
    def repeatedNTimes(self, A):
        sum = 0
        for i in A:
            for j in range(len(A)):
               if i == A[j]:
                sum += 1
            if sum == len(A) / 2:
                return i
            else:
                sum = 0
        