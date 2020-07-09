# class Solution(object):
#     @staticmethod
#     def bracket_matcher(lpar, rpar):
#         br_map = {
#             "{": "}",
#             "[": "]",
#             "(": ")"
#         }
#         return (lpar in br_map and br_map[lpar] == rpar)

#     def isValid(self, s):
#         bracket_stack = []
#         for k in s:
#             if len(bracket_stack) == 0:
#                 bracket_stack.append(k)
#             elif Solution.bracket_matcher(bracket_stack[-1], k):
#                 bracket_stack.pop()
#             else:
#                 bracket_stack.append(k)
#         return len(bracket_stack) == 0

class Solution(object):
    @staticmethod
    def bracket_matcher(lpar, rpar):
        br_map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        return (lpar in br_map and br_map[lpar] == rpar)

    def isValid(self, s):
        i = 1
        last_idx = 0
        if s is None or len(s) == 1:
            return False
        while i < len(s) and len(s) > 0:
            if last_idx == -1:
                last_idx = i
                i += 1
                continue
            if Solution.bracket_matcher(s[last_idx], s[i]):
                # Modify the original string accordingly
                s = s[:last_idx] + s[i+1:]
                i = last_idx - 1
                last_idx = -1
            else:
                last_idx = 1
            i += 1
        return last_idx == -1

