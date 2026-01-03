# Leetcode 16 - 3 Sum Closest
# Score: 106/106 testcases passed
# Solution: Sort the array. Run 3 sum algorithm from Leetcode 15. If a number adds to 0, return 0, otherwise calculate "distance". At the end return closest sum
# 

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        manipulatedArr = nums
        manipulatedArr.sort()
        arrLen = len(manipulatedArr)
        closest = 100000
        returnSum = 0
        for i in range(arrLen):
            varA = manipulatedArr[i]
            startIndex = i+1
            endIndex = arrLen-1
            while startIndex < endIndex:
                varB = manipulatedArr[startIndex]
                varC = manipulatedArr[endIndex]
                sum = varA + varB + varC
                if sum == target:
                    return sum
                elif sum < target:
                    startIndex += 1
                elif sum > target:
                    endIndex -= 1
                difference = abs(target - sum)
                if difference < closest:
#                    print(f"A:{varA} B:{varB} C:{varC}")
                    returnSum = sum
                    closest = difference
        return returnSum


testArr = [4,0,5,-5,3,3,0,-4,-5]
#testArr = [-100,-70,-60,110,120,130,160]
testCase = Solution()
print(testCase.threeSumClosest(testArr, -2))

