# https://leetcode.com/problems/get-equal-substrings-within-budget/description/

# You are given two strings s and t of the same length and an integer maxCost.
# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

#  Example 1:

# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd".
# That costs 3, so the maximum length is 3.


# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         n = len(s)
#         start = 0
#         current_cost = 0
#         max_length = 0

#         for end in range(n):
#             current_cost += abs(ord(s[end]) - ord(t[end]))

#             while current_cost > maxCost:
#                 current_cost -= abs(ord(s[start]) - ord(t[start]))
#                 start += 1

#             max_length = max(max_length, end - start + 1)
        
#         return max_length
     
# sol = Solution()
# print(sol.equalSubstring())


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = len(s)
        left = cost = max_l = 0

        for right in range(l):
            cost += abs(ord(s[right]) - ord(t[right]))

            while(cost > maxCost):
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_l = max(max_l, right - left + 1)
        
        return max_l
    