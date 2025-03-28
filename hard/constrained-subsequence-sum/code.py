import heapq

class Solution(object):
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0

        max_sum = nums[0]
        max_heap = [(-nums[0], 0)]

        i = 1
        while i < len(nums):
            # Prune larger distanced values from max position since we are only
            # concerned with the max value
            while max_heap[0][1] < i - k:
                heapq.heappop(max_heap)

            # If top of heap is negative then that means all elements
            # to the left of current in vicinity are negative. Hence
            # we use 0 there.
            curr_sum = nums[i] + max(0, -max_heap[0][0])
            max_sum = max(max_sum, curr_sum)

            # Add value to max heap and do pruning of more distanced values
            # We update the curr sum to carry over the information
            heapq.heappush(max_heap, (-curr_sum, i))

            i += 1

        return max_sum




# Old approach 1
# class Solution(object):
#     def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
#         if k == 1:
#             return max(nums)

#         greedy_select = []
#         s_index = 0
#         s_sum = nums[0]
#         while s_index < len(nums):
#             if nums[s_index] >= 0:
#                 s_sum = nums[s_index]
#                 break # We have a good number to start with
#             else:
#                 # Continue collecting maximum negative number
#                 s_sum = max(s_sum, nums[s_index])
#             s_index += 1


#         greedy_select.append(s_sum)

#         # We now have a start point
#         while True:
#             s_right_max_excl = s_index + k + 1
#             s_right_max_excl = min(len(nums), s_right_max_excl)

#             i = s_index + 1
#             l_index = i
#             l_value = nums[l_index]
#             while i < s_right_max_excl:
#                 '''
#                 For every number, if its is:
#                 - >= 0 then imm use it
#                 - < 0 then take the largest neg number
#                 '''
#                 if nums[i] >= 0:
#                     l_value = nums[i]
#                     l_index = i
#                     break
#                 elif l_value <= nums[i]:
#                     l_value = nums[i]
#                     l_index = i
#                 i += 1

#             # We now have the largest number that qualifies
#             greedy_select.append(l_value)
#             s_index = l_index

#             if s_index >= len(nums) - 1:
#                 break

#         print(greedy_select)
#         op_sum = sum(greedy_select)
#         if len(greedy_select) > 1 and greedy_select[-1] < 0:
#             op_sum = max(op_sum, sum(greedy_select[:-1]))

#         return op_sum



