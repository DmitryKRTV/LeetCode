# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/

# Given an array of integers arr.

# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

# Let's define a and b as follows:

#     a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
#     b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

# Note that ^ denotes the bitwise-xor operation.

# Return the number of triplets (i, j and k) Where a == b.

# Example 1:

# Input: arr = [2,3,1,6,7]
# Output: 4
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

# IDEA: if a == b it means a ^ b == 0, so we need to find all subarrays that XOR to 0; every such subarray with N elements
#       can be split into N-1 triplets (since we can't have empty 'a' or 'b'); use nested loop to find all subarrays
#       O(N^2) time, O(1) space
#

def countTriplets(self, arr: list[int]) -> int:
    res = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            xor ^= arr[j]
            if xor == 0:
                res =+j - i
    return res