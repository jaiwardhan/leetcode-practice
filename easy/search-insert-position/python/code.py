class Solution(object):
    @staticmethod
    def find_idx(nums, target):
        s = 0
        e = len(nums) - 1
        last_s = s

        while s <= e:
            mid = int((s+e)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                last_s = mid
                s = mid + 1
        
        return last_s


    def searchInsert(self, nums, target):
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1
        idx = Solution.find_idx(nums, target)
        return idx if nums[idx] == target else (idx if nums[idx] > target else idx + 1)