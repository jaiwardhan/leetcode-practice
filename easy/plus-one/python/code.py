class Solution(object):
    def plusOne(self, digits):
        carry = 1
        i = len(digits) - 1
        while i >= 0 and carry > 0:
            digits[i] += (carry)
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
            i -= 1
        if carry > 0:
            return [carry] + digits
        return digits