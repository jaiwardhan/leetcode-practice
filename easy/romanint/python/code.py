class Solution(object):
    def __init__(self):
        self.roman_maps = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def n(self, code):
        if str(code) not in self.roman_maps:
            return 0
        return self.roman_maps[str(code)]
    
    @staticmethod
    def digits(num):
        digs = 0
        if num < 0:
            num = num * (-1)
        while num != 0:
            digs += 1
            num = int(num/10)
        return digs

    def romanToInt(self, s):
        curr_num = 0
        previous_num = 0
        previous_char = ""
        for k in s:
            if previous_char == "":
                previous_char = k
                previous_num = self.n(previous_char)
                continue
            if self.n(previous_char) == self.n(k):
                # Same number should be added
                previous_num = previous_num + self.n(k)
            elif self.n(previous_char) > self.n(k):
                # Big to small, hence add to main
                pre_digits = Solution.digits(self.n(k))
                curr_num += previous_num
                previous_num = self.n(k)
                previous_char = k
            else:
                # Small to large, subtract from prev
                previous_num = self.n(k) - previous_num
                previous_char = k
        
        curr_num += previous_num
        return curr_num

