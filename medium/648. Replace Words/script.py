# https://leetcode.com/problems/replace-words/description/?envType=daily-question&envId=2024-06-07

# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
# `Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
# Return the sentence after the replacement.

# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"`

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        s = sorted(dictionary, key=len)
        res = []
        for w in sentence.split(' '):
            add = w
            min = len(w)
            for root in s:
                if root in w and w.index(root) < min and w.index(root) == 0:
                    add = root
                    min = w.index(root)
                
            res.append(add)

        return ' '.join(res)
    
class Solution2:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionary.sort(key=len)
        lst = sentence.split()
        for root in dictionary:
            for index, word in enumerate(lst):
                if word.startswith(root):
                    lst[index] = root
        return ' '.join(lst)
    
print(Solution().replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
# print(Solution().replaceWords(["ab", "a"], "ccab ba"))