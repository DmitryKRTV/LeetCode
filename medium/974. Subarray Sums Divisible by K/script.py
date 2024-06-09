# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/?envType=daily-question&envId=2024-06-09

# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

class SolutionBrut:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        r = 0
        sum = 0
        for i in range(len(nums)):
            sum = nums[i]
            if (sum % k == 0): 
                r += 1
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                if (sum % k == 0): 
                    r += 1
        return r

print(SolutionBrut().subarraysDivByK([1, 3, -3], 3))

class SolutionPrefixSum:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        reminders = {0: 1}
        res = 0
        prefix_sum_sum = 0

        for num in nums:
            prefix_sum_sum +=num
            reminder = prefix_sum_sum % k
            if reminder in reminders:
                res += reminders[reminder]
            reminders[reminder] = reminders.get(reminder, 0) + 1
        return res



print(SolutionPrefixSum().subarraysDivByK([1, 3, -3], 3))