import unittest
import HtmlTestRunner

from Cell2D import *

from Prediction import *
w= 'n'
class Test(unittest.TestCase):
    def setUp(self):
        self.FP = FirePlace1.wind
        self.Map =FirePlace1.place
        self.prob = [Water_prob,Road_Prob,Wood_House_Prob]
        self.No_Fire = [[80,90],[10,12]]
        self.firefighter_loc = Fighter
        self.size = [n,m]
        self.iter = n
    def testcase1(self):
        section = list(set(FirePlace1.wind).intersection(wind_condition))
        self.assertTrue(len(section)==1,'wind condition eneter incorrect')
    def testcase2(self):
        self.assertTrue(np.shape(self.Map)==(n,m),'size not match')
    def testcase3(self):
        for i in self.prob:
            self.assertTrue(i>=0,'prob for can not be negative')
    def testcase4(self):
        for i in range(self.No_Fire[0][0],self.No_Fire[0][1]):
            for j in range(self.No_Fire[1][0],self.No_Fire[1][1]):
                self.assertTrue(FirePlace1.place[i,j]==0.,'Requirement 3: cell with zero probability cannot burn')
    def testcase5(self):
        for i in range(len(self.firefighter_loc)):
            self.assertTrue(FirePlace1.place[self.firefighter_loc[i][0],self.firefighter_loc[i][1]]!=1,'firefigher deployed in the fire')
            self.assertLess(self.firefighter_loc[i][0],self.size[0],'firefighter {} value {}out of simulation range'.format(i,self.firefighter_loc[i][0]))
            self.assertLess(self.firefighter_loc[i][1],self.size[1],'firefighter {} value {}out of simulation range'.format(i,self.firefighter_loc[i][1])
    def testcase6(self):
        self.assertLess(self.size[0],10000,'simluation size too big')
        self.assertLess(self.size[1],10000,'simluation size too big')
        self.assertGreater(self.size[0],10,'simluation size too small')
        self.assertGreater(self.size[1],10,'simluation size too small')
        self.assertLess(self.iter,100000,'number of iteration exceeded')
        self.assertGreater(self.iter,0,'need iteration')

unittest.main()

# if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
 