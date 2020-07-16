class Solution(object):
        
    def countAndSay(self, term):
        new_set = [1]
        while term > 1:
            i = 1
            temp_set = []
            last_dig = new_set[0]
            last_freq = 1
            # temp_set = temp_set + ["1", last_dig]
            while i < len(new_set):
                if last_dig == new_set[i]:
                    last_freq += 1
                else:
                    temp_set = temp_set + [last_freq, last_dig]
                    last_dig = new_set[i]
                    last_freq = 1
                i += 1
            temp_set = temp_set + [last_freq, last_dig]
            new_set = temp_set
            term -= 1
        
        res = ""
        for k in new_set:
            res += str(k)
        return res