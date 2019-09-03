class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        li = []
        out = []
        for i in range(left,right+1):
            li.append(i)
        for i in li:
            if i < 10:
                out.append(i)
            if 10<i<100:
                if i%10 != 0:
                    if i%(i/10) == 0 and i%(i%10) == 0:
                        out.append(i)
            if 100<i<1000:
                if i%10 != 0 and (i%100) > 10:
                    if i%(i/100) == 0 and i%((i/10)%10) == 0 and i%(i%10) == 0:
                        out.append(i)
            if 1000 < i < 10000:
                if i%10 != 0 and (i%100) > 10 and (i%1000) > 100:
                    if i%(i/1000) == 0 and i%((i/100)%10) == 0 and i%((i/10)%10) == 0 and i%(i%10) == 0:
                        out.append(i)
        return out
                        

        