# This is a test runner driver suite.
# Tweak this per problem basis

from code import Solution
import json

class TestDriver:
    def __init__(self):
        print ( "Loading Test file.." )
        self.all_pass = True
        self.total_cases = 0
        self.total_pass = 0
        self.total_fail = 0
        self.total_notrun = 0
        with open("./test.json") as f:
            self.test_file = json.loads(f.read())
            f.close()
    
    def test_pass(self, test_number):
        print ( " [_/] Test case passed: %d" % (int(test_number)))
        self.total_pass += 1

    def test_fail(self, test_number, expected, found):
        print ( " [x] Test case failed: %d. Expected %s, found %s" % (int(test_number), str(expected), str(found)))
        self.all_pass = False
        self.total_fail += 1

    def test_verdict(self):
        if self.all_pass:
            print ( ":: All cases have passed: (Total: %d, Pass: %d, Fail: %d), Accu %s" % (
                self.total_cases,
                self.total_pass,
                self.total_fail,
                str(self.total_pass*100 / self.total_cases)+"%"
            ))
        else:
            print (":: Some cases have failed!")

    def load_tests(self):
        print ( "Loading tests.." )
        self.tests = self.test_file["tests"]
        self.test_desc = self.test_file["description"]
        self.total_cases = len(self.tests)
    
    def test(self):
        print ( "Starting tests.." )
        s = Solution()
        for k,v in enumerate(self.tests):
            res = s.isPalindrome(v["inputs"][0])
            if res != v["outputs"][0]:
                self.test_fail(k, v["outputs"][0], res)
            else:
                self.test_pass(k)
        self.test_verdict()

t = TestDriver()
t.load_tests()
t.test()
    
    