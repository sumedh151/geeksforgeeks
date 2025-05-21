# https://www.geeksforgeeks.org/problems/sum-of-elements-between-k1th-and-k2th-smallest-elements3133/0
#User function Template for python3

class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Your code goes here
        import heapq
        heap1 = [] # length k1 
        heap2 = [] # length k2 - k2 - 1
        for i in range(N):
            heapq.heappush(heap1, -A[i])
            if len(heap1)>K1:
                popped = -heapq.heappop(heap1)
                heapq.heappush(heap2, -popped)
            if len(heap2)>K2-(K1+1):
                heapq.heappop(heap2)
        sum_elems = 0
        while(heap2):
            sum_elems += -heapq.heappop(heap2)
        return sum_elems


# Given an array A[] of N positive integers and two positive integers K1 and K2. 
# Find the sum of all elements between K1th and K2th smallest elements of the array. It may be assumed that (1 <= k1 < k2 <= n).

# Example 1:
# Input:
# N  = 7
# A[] = {20, 8, 22, 4, 12, 10, 14}
# K1 = 3, K2 = 6
# Output:
# 26
# Explanation:
# 3rd smallest element is 10
# 6th smallest element is 20
# Element between 10 and 20 
# 12,14. Their sum = 26.
 

# Example 2:
# Input
# N = 6
# A[] = {10, 2, 50, 12, 48, 13}
# K1= 2, K2 = 6
# Output:
# 73
