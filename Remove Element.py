class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in nums:
            if i == val:
                count+=1
        for i in range(0,count):
            nums.remove(val)