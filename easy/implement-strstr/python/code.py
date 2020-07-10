class Solution(object):
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
            
    def strStr(self, haystack, needle):
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