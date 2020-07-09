class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        i = 0
        while i < len(nums):
            if nums[i] not in lookup:
                # no early pair found
                # add this to the lookup
                lookup[target-nums[i]] = i
            else:
                return [lookup[nums[i]], i]
            i = i + 1
        return [-1, -1]