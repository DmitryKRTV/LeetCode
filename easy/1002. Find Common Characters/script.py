# https://leetcode.com/problems/find-common-characters/description/

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        c = Counter(words[0])
        r = []
        for w in words[1:]:
            c &= Counter(w)
        for l, i in c.items():
            r.extend([l] * i)
        return r

print(Solution().commonChars(["bella","label","roller"]))
