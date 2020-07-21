class Solution(object):
    def checkPossibility(self, nums):
        faults = 0
        ll = len(nums)
        if ll <= 2:
            return True
        
        i = 0
        while i < ll - 2 and faults < 2:
            if nums[i] > nums[i+1]:
                # check which type trench this is
                if nums[i+2] >= nums[i]:
                    # nums i+1 is editable to be a min of nums[i]
                    faults += 1
                    nums[i+1] = nums[i]
                elif nums[i+2] >= nums[i+1]:
                    if i == 0:
                        nums[i] = nums[i+1]
                        faults += 1
                    elif nums[i-1] <= nums[i+1]:
                        nums[i] = nums[i-1]
                        faults += 1
                    # tentative deep trench and needs minimum
                    # of 2 edits
                    else:
                        return False
                else:
                    # this is a deep trench and needs a minimum
                    # of 2 edits
                    return False
            i += 1
        
        if faults < 2:
            if nums[i] > nums[i+1]:
                faults += 1

        return faults < 2

# class Solution(object):
#     def checkPossibility(self, nums):
#         size_of_nums = len( nums )
#         if size_of_nums <= 1:
#             return True
#         faults = 0

#         # scan each element, and compare to neighbor
#         for i in range( size_of_nums - 1 ):
#             if nums[i] > nums[i+1]:
#                 if faults >= 1:
#                     return False
#                 faults += 1
#                 if (i-1) < 0 or nums[i-1] <= nums[i+1] :
#                     nums[i] = nums[i+1]
#                 else:
#                     nums[i+1] = nums[i]

#         return faults < 2
