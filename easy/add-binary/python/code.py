class Solution(object):
    def addBinary(self, a, b):
        ll_1 = len(a) - 1
        ll_2 = len(b) - 1
        c = ""
        carry = False
        while ll_1 >= 0 and ll_2 >= 0:
            # 1 1 c:1 => 1 + c:1
            # 1 0/0 1 c:1 => 0 + c:1
            # 0 0 c:1 => 1 + c:0
            if carry:
                if a[ll_1] == "1" and b[ll_2] == "1":
                    carry = True
                    c = c + "1"
                elif a[ll_1] == "0" and b[ll_2] == "0":
                    c = c + "1"
                    carry = False
                else:
                    c = c + "0"
            # 1 1 c:0 => 0 c:1
            # 1 0 / 0 1 c:0 => 1 c:0
            # 0 0 c:0 => 0 c:0
            else:
                if a[ll_1] == "1" and b[ll_2] == "1":
                    carry = True
                    c = c + "0"
                elif a[ll_1] == "0" and b[ll_2] == "0":
                    carry = False
                    c = c + "0"
                else:
                    c = c + "1"
                    carry = False
            ll_1 -= 1
            ll_2 -= 1
        if ll_1 >= 0:
            while ll_1 >= 0:
                if carry:
                    if a[ll_1] == "0":
                        c = c + "1"
                        carry = False
                    else:
                        c = c + "0"
                else:
                    c = c + a[ll_1]
                ll_1 -= 1
        if ll_2 >= 0:
            while ll_2 >= 0:
                if carry:
                    if b[ll_2] == "0":
                        c = c + "1"
                        carry = False
                    else:
                        c = c + "0"
                else:
                    c = c + b[ll_2]
                ll_2 -= 1
        if carry:
            c = c + "1"
        return c[::-1]
