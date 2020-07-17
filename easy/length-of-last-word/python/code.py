class Solution(object):
    def lengthOfLastWord(self, s):
        last_sp_ix = -1
        lw = 0
        i = 0
        s = s + "*"
        while s[i] != "*":
            if s[i] == " ":
                if i - last_sp_ix -1 > 0:
                    lw = i - last_sp_ix - 1
                last_sp_ix = i
            i += 1
        if last_sp_ix < i-1:
            lw = i - last_sp_ix - 1
        
        return lw