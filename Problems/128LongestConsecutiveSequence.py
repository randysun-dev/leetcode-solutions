# Leetcode 70 - Climbing Stairs
# Score: 45/45 testcases passed
# Solution: Fibonacci Sequence
# Learning: Sort and iterate through list to count longest sequence.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        longestCons = 0
        count = 1

        if len(nums) == 1:
            return 1
    
        for i in range(len(nums)-1):
            if (nums[i+1]-nums[i] == 1):
                count += 1
            elif(nums[i+1]-nums[i] != 0):
                count = 1
            if count > longestCons:
                longestCons = count
        return longestCons
        
    
#test = [100,4,200,1,3,2]
test = [1,0,1,2]
testCase = Solution()
print(testCase.longestConsecutive(test))

