# https://leetcode.com/problems/ransom-note/description/

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = magazine
        for l in ransomNote:
            if l in m: 
                m = m.replace(l, '', 1)
            else: return False
        return True
    
class BestSolution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False

sol = Solution()

print(sol.canConstruct('aa', 'aab'))