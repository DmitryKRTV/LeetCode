# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/?envType=daily-question&envId=2024-05-29

# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
#     If the current number is even, you have to divide it by 2.
#     If the current number is odd, you have to add 1 to it.
# It is guaranteed that you can always reach one for all test cases.


# Example 1:

# Input: s = "1101"
# Output: 6
# Explanation: "1101" corressponds to number 13 in their decimal representation.
# Step 1) 13 is odd, add 1 and obtain 14. 
# Step 2) 14 is even, divide by 2 and obtain 7.
# Step 3) 7 is odd, add 1 and obtain 8.
# Step 4) 8 is even, divide by 2 and obtain 4.  
# Step 5) 4 is even, divide by 2 and obtain 2. 
# Step 6) 2 is even, divide by 2 and obtain 1.  

class Solution:
    def numSteps(self, s: str) -> int:
        # d = int(s, 2)
        # res = 0
        # while (d > 1):
        #     if d % 2 == 0: d //= 2
        #     else: d += 1
        #     res += 1
        # return res
        step = 0
        carry = 0
        for i in s[::-1][:-1]:
            if int(i) + carry == 1:
                carry = 1
                step += 2
            else: 
                step += 1
        return step + carry

print(Solution().numSteps('1111011110000011100000110001011011110010111001010111110001'))

