# Leetcode 15 - 3Sum
# Score: 310/315 testcases passed
# Solution: Sort the array. 3 for loops. Fixed first num, fix 2nd num, see if third number is in array, if so, add all three to final result.
# Learning: This approach took too long for large loops. Reducing complexity to two loops if possible.




class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        returnArr = []
        manipulatedArr = nums
        arrLen = len(manipulatedArr)
        for i in range(arrLen):
            fixedA = manipulatedArr[i]
            if fixedA <= 0:
                for j in range(arrLen):
                    if i < j:
                        fixedB = manipulatedArr[j]
                        for k in range(arrLen):
                            if j < k:
                                fixedC = manipulatedArr[k]
                                if fixedA + fixedB + fixedC == 0:
                                    tempArr = [fixedA, fixedB, fixedC]
                                    tempArr.sort()
                                    if not (tempArr in returnArr):
                                        returnArr.append(tempArr)

        return returnArr

#testArr = [-1,0,1,2,-1,-4]
testArr = [-100,-70,-60,110,120,130,160]
testCase = Solution()
print(testCase.threeSum(testArr))