# Leetcode 07 - Reverse Integer
# Score: 1045/1045 testcases passed
# Solution: Convert integer to string, then reverse it, convert it back to int, handle min/max int edge cases
# Learning: Forgot to handle negative values at first.

# Given a signed 32-bit integer xreturn x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

MIN_SIGNED_INT32 = -2147483648
MAX_SIGNED_INT32 = 2147483647

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNeg = False
        intToStr = x
        if x < 0:
            isNeg = True
            intToStr *= -1
        
        stringValue = str(intToStr)
        reverseString = ""
        
        stringLen = len(stringValue)
        for i in range(stringLen):
            reverseString += stringValue[stringLen-1-i]
        reverseInt = int(reverseString)
        if isNeg:
            reverseInt *= -1
        if MIN_SIGNED_INT32 <= reverseInt and MAX_SIGNED_INT32 >= reverseInt:
            return reverseInt
        else:
            return 0

testInt = -123
testCase = Solution()
print(testCase.reverse(testInt))