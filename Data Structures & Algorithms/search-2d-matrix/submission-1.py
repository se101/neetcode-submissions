class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, len(matrix)-1
        row = 0
        while start <= end:
            middle = (start+end)//2
            if matrix[middle][0]>target:
                end = middle-1
            else:
                row = middle
                start = middle+1
        left, right = 0, len(matrix[0])-1
        while left<=right:
            middle = (left+right)//2
            if matrix[row][middle]> target:
                right = middle-1
            elif matrix[row][middle]<target:
                left=middle+1
            else:
                return True
        return False