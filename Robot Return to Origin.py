class Solution(object):
    def judgeCircle(self, moves):
        U = moves.count('U')
        D = moves.count('D')
        L = moves.count('L')
        R = moves.count('R')
        
        if U == D and L == R:
            return True
        else:
            return False