# This is a test runner driver suite.
# Tweak this per problem basis

from code import Solution
import json

class TestDriver:
    def __init__(self):
        print ( "Loading Test file.." )
        with open("./test.json") as f:
            self.test_file = json.loads(f.read())
            f.close()
    
    def load_tests(self):
        print ( "Loading tests.." )
        self.tests = self.test_file["tests"]
        self.test_desc = self.test_file["description"]
    
    def test(self):
        print ( "Starting tests.." )
        s = Solution()
        all_pass = "YES"
        for i,t in enumerate(self.tests):
            ret = s.reverse(t["inputs"])
            if ret == t["outputs"]:
                print (" [_/] : Passed Case %d" % (i))
            else:
                print (" [x] : Failed Case %d => Found %d, Expected %d" % (i, ret, t["outputs"]))
                all_pass = "NO"
        print ( ":: All cases passed: %s" % all_pass)

        

t = TestDriver()
t.load_tests()
t.test()
    
    