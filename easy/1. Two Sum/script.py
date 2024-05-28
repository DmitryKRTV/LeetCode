# https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in d: 
                return [d[tmp], i]
            d[nums[i]] = i
        return []


class Brut:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    

sol = Solution
print(sol.twoSum([2,7,11,15], 6))