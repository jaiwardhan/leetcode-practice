# This is a test runner driver suite.
# Tweak this per problem basis

from code import Solution, ListNode
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
            print ( ":: All cases have passed!")
        else:
            print (":: Some cases have failed!")
        print ( "Total: %d, Pass: %d, Fail: %d, [Accu %s]" % (
                self.total_cases,
                self.total_pass,
                self.total_fail,
                str(self.total_pass*100 / self.total_cases) +"%"
            ))

    def load_tests(self):
        print ( "Loading tests.." )
        self.tests = self.test_file["tests"]
        self.test_desc = self.test_file["description"]
        self.total_cases = len(self.tests)
    
    def test(self):
        print ( "Starting tests.." )
        s = Solution()
        for i,t in enumerate(self.tests):
            expected = t["outputs"]
            l1 = ListNode.parse_into_node(t["inputs"][0])
            l2 = ListNode.parse_into_node(t["inputs"][1])
            res = s.mergeTwoLists(l1, l2)
            if ListNode.list_matches_node(expected, res):
                self.test_pass(i)
            else:
                self.test_fail(i, expected, ListNode.parse_from_node(res))
        self.test_verdict()
        

t = TestDriver()
t.load_tests()
t.test()
    
    