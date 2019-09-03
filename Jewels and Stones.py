class Solution(object):
    def numJewelsInStones(self, J, S):
        sum = 0
        for i in S:
            if i in J:
                sum += 1
        return sum
        