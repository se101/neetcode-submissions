class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix)-1
        while start<=end:
            middle = (start+end)//2
            print(start, end, middle)
            if matrix[middle][0]>target:
                end = middle-1
            elif matrix[middle][-1]<target:
                start=middle+1
            else:
                left, right = 0, len(matrix[middle])-1
                while left<=right:
                    middle1 = (left+right)//2
                    if matrix[middle][middle1]>target:
                        right-=1
                    elif matrix[middle][middle1]<target:
                        left+=1
                    else:
                        return True
                return False
        return False
        
            
