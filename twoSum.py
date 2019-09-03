class Solution(object):
    def twoSum(self, nums, target):
        count = 0
        for i in range(len(nums)):
            if (target-nums[i]) in nums :
                if nums[i] == target-nums[i]:
                    for k in range(len(nums)):
                        if nums[k] == nums[i]:
                            count += 1
                            indexxx = k
                    if count > 1:
                            return[i,indexxx]
                    else:
                        continue
                break
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]== target :
                break
        return[i,j]
