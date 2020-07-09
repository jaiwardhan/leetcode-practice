class Solution(object):
    def longestCommonPrefix(self, strs):
        # If empty list, there is no LCP
        if len(strs) == 0:
            return ""
        # List containing one signle item is LCP itself
        if len(strs) == 1:
            return strs[0]
        
        ini = ""
        maxlen = 0
        ref_char = ""
        exit_all = False

        # For every index starting 0, check if all strings 
        # have the same character at that index as strs[0].
        # If all match, append to the result, else break
        # and return the last known result.
        # Complexity: O(n*k) // n=number of strings, k=maxlen of lcp
        # Worst case: O(n^2)
        while True:
            if maxlen < len(strs[0]):
                ref_char = strs[0][maxlen]
            else:
                exit_all = True
                break
            for k in strs:
                if maxlen < len(k) and ref_char == k[maxlen]:
                    continue
                else:
                    # we are done
                    exit_all = True
                    break
            if exit_all:
                break
            ini += ref_char
            maxlen += 1
        return ini