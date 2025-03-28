# This is a test runner driver suite.
# Tweak this per problem basis

from code import Solution
import json
import time

class TestDriver:
    def __init__(self):
        print ( "Loading Test file.." )
        self.all_pass = True
        self.total_cases = 0
        self.total_pass = 0
        self.total_fail = 0
        self.total_notrun = 0
        self.time_taken = []
        with open("./test.json") as f:
            self.test_file = json.loads(f.read())
            f.close()
    
    def evaluate_time_ms(self, start_time, end_time):
        dif = end_time - start_time
        dif = dif*1000000 #convert s to ms
        return dif

    def test_pass(self, test_number, start_time = None, end_time = None):
        if start_time is None or end_time is None:
            print ( " [_/] Test case passed: %d" % (int(test_number)))
        else:
            tt = self.evaluate_time_ms(start_time, end_time)
            print ( " [_/] Test case passed: %d, Time taken: %4.2f ms" % (int(test_number), tt))
            self.time_taken.append(tt)
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
        if len(self.time_taken) > 0:
            sum = 0.0
            for i in self.time_taken:
                sum += i
            print ( "> Avg time taken %4.2f ms" % (sum/len(self.time_taken)))
            print ( "> Total time taken %4.2f ms" % (sum))

    def load_tests(self):
        print ( "Loading tests.." )
        self.tests = self.test_file["tests"]
        self.test_desc = self.test_file["description"]
        self.total_cases = len(self.tests)
        self.to_debug = self.test_file["debug_tests"] if "debug_tests" in self.test_file else []
    
    def test(self):
        print ( "Starting tests.." )
        s = Solution()
        to_test = self.tests
        if len(self.to_debug) > 0:
            to_test = []
            for to_debug_test_nums in self.to_debug:
                to_test.append(self.tests[to_debug_test_nums])
            print ("###################################################")
            print ("[!] Would be debugging the following tests: ")
            print (self.to_debug)
            print ("###################################################")
            print ("")

        for i,t in enumerate(to_test):
            time_start = time.time()
            # use t["inputs"][0] etc to pass parameters
            # use t["outputs"][0] etc to compare with outputs
            # Set expected = t["outputs"][0] etc and to ensure logging
            # Set found as result of solution and to ensure logging
            expected = t["outputs"][0]
            ##### your execution here #####
            found = s.constrainedSubsetSum(t["inputs"][0], t["inputs"][1])
            ###############################
            time_end = time.time()
            if found == expected:
                self.test_pass(i, time_start, time_end)
            else:
                self.test_fail(i, expected, found)

            # if test passes
            # self.test_pass(i, time_start, time_end)

            # if test fails
            # self.test_fail(i, expected, found)
        self.test_verdict()

t = TestDriver()
t.load_tests()
t.test()
    
    