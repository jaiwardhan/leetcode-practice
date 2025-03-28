class Solution(object):
    def longestSubarray(self, nums: list[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        index_l = 0
        index_r = 1
        count_0s = 1 if nums[index_l] == 0 else 0
        index_partition_0 = 0 if count_0s > 0 else 1

        max_1s = 0

        while index_r < len(nums):
            if nums[index_r] == 0:
                count_0s += 1
                # If this is a second 0, record max and slide from partition
                if count_0s > 1:
                    max_1s = max(max_1s, index_r - index_l - 1)
                    # Slide
                    index_l = index_partition_0 + 1
                    index_partition_0 = index_r
                    count_0s = 1
                else:
                    # First 0 occurrence, set partition
                    index_partition_0 = index_r

            index_r += 1

        last_len = (len(nums) - index_l) - (1 if count_0s > 0 else 1)
        max_1s = max(max_1s, last_len)
        return max_1s
