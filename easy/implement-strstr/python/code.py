class Solution(object):
    def __init__(self):
        self.critical_threshold_factor = 90
    @staticmethod
    def matcher(needle, n_start, n_end, haystack, h_start, h_end):
        found = True
        while h_start < h_end and n_start < n_end:
            if needle[n_start] != haystack[h_start]:
                found = False
                break
            h_start += 1
            n_start += 1
        return found, h_start
    
    def naive(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None or len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        i = 0
        while i < len(haystack) - len(needle) + 1:
            found, _ = Solution.matcher(needle, 0, len(needle), haystack, i, len(haystack))
            if found:
                return i
            i += 1
        return -1

    def strStr(self, haystack, needle):
        if haystack is None or needle is None:
            return 0
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        len_haystack = len(haystack)
        if len_needle > len_haystack:
            return -1
        if len_needle == 1:
            return -1 if needle[0] != haystack[0] else 0


        if int(len_needle*100 / len_haystack) > self.critical_threshold_factor:
            return self.naive(haystack, needle)

        # Pi table: Preprocess the needle
        pi_table = [0]*len_needle

        '''
        ababcab => [0, 0, 1, 2, 0, 1, 2]
        '''
        i = 1
        previous_len = 0
        while i < len_needle:
            if needle[i] == needle[previous_len]:
                previous_len += 1
                pi_table[i] = previous_len
                i += 1
            else:
                if previous_len != 0:
                    previous_len = pi_table[previous_len - 1]
                else:
                    pi_table[i] = 0
                    i += 1

        '''
        Do the KMP search now
        '''
        i = 0
        j = 0
        while i < len_haystack:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len_needle:
                    return i - j
            else:
                if j != 0:
                    j = pi_table[j-1]
                else:
                    i += 1
        return -1
            

