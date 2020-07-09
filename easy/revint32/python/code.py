class Solution(object):
    def reverse(self, x):
        y = 0
        lims_neg = -1*(2**31)
        lims_pos = 2**31 - 1
        signed = False
        if x < 0:
            signed = True
            x = x * (-1)
        # print ("Lims neg & pos %d %d" % (lims_neg, lims_pos))
        while x != 0:
            if y < int(lims_neg / 10) or y > int(lims_pos / 10):
                return 0
            y = y * 10 + int(x % 10)
            x = int(x / 10)
        if signed:
            y = y * (-1)
            signed = False
        return y

        