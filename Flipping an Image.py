class Solution(object):
    def flipAndInvertImage(self, A):
        s = []
        b = []
        for i in A:
            i.reverse()
        for i in A:
            for node in i:
                if node == 0:
                    node =1
                elif node == 1:
                    node = 0
                s.append(node)
            b.append(s)
            s = []
        return b