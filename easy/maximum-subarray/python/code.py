class Solution(object):
    # Kaden's algorithm
    def maxSubArray(self, nums):
        i = 1
        lsum = nums[0]
        ov_max = lsum
        while i < len(nums):
            lsum = lsum + nums[i]
            if lsum < nums[i]:
                lsum = nums[i]
            if lsum > ov_max:
                ov_max = lsum
            i += 1
        return ov_max
        