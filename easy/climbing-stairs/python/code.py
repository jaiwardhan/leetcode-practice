class Solution(object):
    def __init__(self):
        self.hm = {
            0: 1,
            -1: 0,
            -2: 0
        }
    def reset(self):
        self.hm = {
            0: 1,
            -1: 0,
            -2: 0
        }
    def climbStairs(self, n):
        if n in self.hm:
            return self.hm[n]
        self.hm[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.hm[n]