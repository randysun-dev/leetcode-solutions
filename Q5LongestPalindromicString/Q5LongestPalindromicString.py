# Leetcode 05 - Longest Palindromic String
# Score: 143/143 Test Cases Passed
# Solution: generate every substring possible, check if it is palindrome and longest, if so then set returnstring to palindrome
# Learning: Reduced runtime by only checking palindromic substrings that could potentially be the "longest" - string length has
# to exceed the current longest string


# Given a string s, return the longest palindromic substring in s
# example 1
# input: s = "babad"
# output: "bab" or "aba"
 
# example 2
# input: s = "cbbd"
# output: "bb"
 

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        beginIndex = 0
        endIndex = len(s)-1
        while(beginIndex < endIndex):
            if s[beginIndex] != s[endIndex]:
                return False
            beginIndex += 1
            endIndex -= 1
        return True
 
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        returnStr = ""
        stringLength = len(s)
        for i in range(stringLength):
            for j in range(stringLength):
                if j >= i:
                    substring = s[i:j+1]
                    if len(substring) > maxLen:
                        if self.isPalindrome(substring):
                            if len(substring) > maxLen:
                                maxLen = len(substring)
                                returnStr = substring
        return returnStr
 
 
# Testing code, not necessary for the solution.
testString = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
testCase = Solution()
print(testCase.longestPalindrome(testString))