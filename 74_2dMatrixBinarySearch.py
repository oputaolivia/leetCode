class Solution:
    def searchMatrix(self, matrix, target):
        rows, cols= len(matrix), len(matrix[0])
        top, bot= 0, rows-1
        while top <= bot:
            midRow=(top + bot)//2
            if target > matrix[midRow][-1]:
                top = midRow + 1
                
            elif target < matrix[midRow][0]:
                bot= midRow - 1
                
            else:
                break
        if not(top <= bot):
            return False
        
        midRow = (top + bot)//2
        l,r = 0, cols-1
        while l <= r:
            m = (l+r)//2
            if target > matrix[midRow][m]:
                l= m +1
                
            elif target < matrix[midRow][m]:
                r= m-1
                
            else:
                return True
        return False