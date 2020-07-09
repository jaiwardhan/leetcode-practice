class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        y = 0
        x_cpy = x
        while x_cpy != 0:
            y = y*10 + int(x_cpy % 10)
            x_cpy = int(x_cpy/10)
        return x == y