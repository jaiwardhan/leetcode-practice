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
        for k,v in enumerate(self.tests):
            inputs = v["inputs"]
            res = v["outputs"]
            s = Solution()
            op = s.twoSum(inputs[0], inputs[1])
            passes = True and op[0] == res[0] and op[1] == res[1]
            if not passes:
                print (" [x] Test %d: Failed" % k)
            else:
                print (" [_/] Test %d: Passed" % k)

        

t = TestDriver()
t.load_tests()
t.test()
    
    