class Solution(object):
    def maxFrequency(self, nums, k: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        nums.sort()
        
        s_win = nums[0]
        len_win = 1
        index_win_left = 0
        freq_max = 1

        i = 1
        while i < len(nums):
            s_target = nums[i]*(len_win+1)
            s_current = nums[i] + s_win

            cost = s_target - s_current
            if cost <= k:
                # Can afford
                freq_max = max(freq_max, len_win+1)
                
                # Update window
                len_win += 1
                s_win += nums[i]
            else:
                # Cannot afford, shift the window with reset
                # most likely we have a maxim window
                freq_max = max(freq_max, len_win)
                s_win = s_win - nums[index_win_left] + nums[i]
                index_win_left += 1
                # Len remains the same

            i += 1

        return freq_max


    def problem(self):
        pass
