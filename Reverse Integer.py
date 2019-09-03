class Solution(object):
    def reverse(self, x):
        stringx = str(x)
        li = []
        temp = []
        for i in stringx:
            li.append(i)
        li.reverse()
        if li == ["0"]:
            return 0
        for i in range(len(li)):
            if li[0] =="-":
                continue
            if li[i] == "0":
                temp.append(i)
            else:
                break
        for i in range(len(temp)):
            del li[0]
        if li[-1] == "-":
            del li[-1]
            li.insert(0,'-')
        stringx = ""
        for i in li:
            stringx += i
        if (int(stringx)>2147483647) or (int(stringx) < -2147483647):
            return 0
        else:
            return int(stringx)
        
