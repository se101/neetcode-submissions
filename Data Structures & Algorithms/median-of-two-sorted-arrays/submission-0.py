class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B)<len(A):
            A,B = B,A
        total = len(nums1)+len(nums2)
        half = total//2
        left, right = 0, len(A)-1
        while True:
            middle = (left+right)//2
            middle1 = half-middle-2
            left1 = A[middle] if middle>=0 else float("-inf")
            right1 = A[middle+1] if middle+1<len(A) else float("inf")
            left2 = B[middle1] if middle1>=0 else float("-inf")
            right2 = B[middle1+1] if middle1+1<len(B) else float("inf")
            #print(subarray1, subarray2)
            if left1<=right2 and left2<=right1:
                if total%2==0:
                    return (max(left1, left2) + min(right1, right2))/2
                else:
                    return min(right1,right2)
            elif left1>right2:
                right = middle-1
            else:
                left = middle+1
        return 

