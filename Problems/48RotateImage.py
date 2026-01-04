# Leetcode 48 - Rotate Image
# Score: / testcases passed
# Solution: Quadrant based. Left Top -> Right Top, Right Top -> Right Bottom, Right Bottom -> Left Bottom, Left Bottom -> Left Top
# Left Top: X = n-X, Y = old X
# Right Top: X = old Y, Y = n-X
# Right Bottom: X = old Y, Y = X
# Learning: 

"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        isOddMatrix = (n % 2 == 1)
        for k in range(int((n+1)/2)):
            for l in range(int((n+1)/2)):
                currX = 0+k
                currY = 0+l
                oldNum = matrix[currY][currX]
                
                for i in range(4):
                    newX = n-currY-1
                    newY = currX
                    saveNum = matrix[newY][newX]
                    #print(f"Current X: {currX}, current Y: {currY}, new X: {newX}, new Y: {newY}")
                    #print(oldNum)
                    matrix[newY][newX] = oldNum
                    currX = newX
                    currY = newY
                    oldNum = saveNum
            
            
            
        print(f"Current X: {currX}, current Y: {currY}, new X: {newX}, new Y: {newY}")
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
#matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
testCase = Solution()
print(testCase.rotate(matrix))

