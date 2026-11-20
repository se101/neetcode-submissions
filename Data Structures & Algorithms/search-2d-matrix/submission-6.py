class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end, middle = 0, rows-1, 0
        while start<=end:
            middle = (start+end)//2
            if matrix[middle][0]>target:
                end = middle-1
            elif matrix[middle][-1]<target:
                start=middle+1
            else:
                break
        left, right = 0, cols-1
        while left<=right:
            middle1 = (left+right)//2
            if matrix[middle][middle1]>target:
                right=middle1-1
            elif matrix[middle][middle1]<target:
                left=middle1+1
            else:
                return True
        return False