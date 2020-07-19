class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        start = 1
        end = x
        ans = 1
        while start <= end:
            mid = int((start+end)/2)
            if mid * mid == x:
                return mid
            elif mid*mid > x: #overshoot
                end = mid - 1
            else:
                start = mid+1
                ans = mid
        return ans


