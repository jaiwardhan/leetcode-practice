class Solution(object):
    def removeDuplicates(self, nums):
        if nums is None:
            return 0
        if len(nums) <= 1:
            return len(nums)
        
        last_unique_idx = 0
        last_unique_val = nums[0]

        i = 1
        while i < len(nums):
            if nums[i] != last_unique_val:
                last_unique_idx += 1
                nums[last_unique_idx] = nums[i]
                last_unique_val = nums[i]
            i+=1
        
        return last_unique_idx+1