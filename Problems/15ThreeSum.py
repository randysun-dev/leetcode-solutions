# Leetcode 15 - 3Sum
# Score: 315/315 testcases passed
# Solution: Sort the array. 2 loops. Fixed first num, start and end index loop.
# Learning: This approach took too long for large loops. Reducing complexity to two loops if possible.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        returnArr = []
        manipulatedArr = nums
        manipulatedArr.sort()
        arrLen = len(manipulatedArr)
        for i in range(arrLen):
            varA = manipulatedArr[i]
            startIndex = i+1
            endIndex = arrLen-1
            while startIndex < endIndex:
                varB = manipulatedArr[startIndex]
                varC = manipulatedArr[endIndex]
                sum = varA + varB + varC
                if sum == 0:
                    tempArr = [varA, varB, varC]
                    tempArr.sort()
                    if not (tempArr in returnArr):
                        returnArr.append(tempArr) 
                    startIndex += 1
                    endIndex -= 1
                elif sum < 0:
                    startIndex += 1
                elif sum > 0:
                    endIndex -= 1
        
        return returnArr


testArr = [-1,0,1,2,-1,-4]
#testArr = [-100,-70,-60,110,120,130,160]
testCase = Solution()
print(testCase.threeSum(testArr))

