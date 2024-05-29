# https://leetcode.com/problems/merge-two-sorted-lists/description/

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2
        res = ListNode(0)
        tmp = res

        while t1 != None and t2 != None:
            if t1.val < t2.val:
                tmp.next = t1
                t1 = t1.next
            else:
                tmp.next = t2
                t2 = t2.next
            
            tmp = tmp.next

        if t1 != None:
            tmp.next = t1
        if t2 != None:
            tmp.next = t2
    
        return res.next