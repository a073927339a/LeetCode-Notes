class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            if target > nums[-1]:
                return len(nums)
            if target < nums[0]:
                return 0
            for i in range(len(nums)):
                if nums[i] < target < nums[i+1]:
                    return i+1