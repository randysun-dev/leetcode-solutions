# Leetcode 70 - Climbing Stairs
# Score: 45/45 testcases passed
# Solution: Fibonacci Sequence
# Learning: Use temp to store modified values

class Solution(object):

    def fibonacci(self, n):
        prevN = 0
        currN = 1
        for i in range(n):
            temp = currN
            currN = currN + prevN
            prevN = temp
            
            
        return currN


    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fibonacci(n)
    
test = 4
testCase = Solution()
print(testCase.climbStairs(4))

