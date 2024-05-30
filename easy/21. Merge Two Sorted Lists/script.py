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
        head = ListNode(0)
        chain = head

        while t1 != None and t2 != None:
            if t1.val < t2.val:
                chain.next = t1
                t1 = t1.next
            else:
                chain.next = t2
                t2 = t2.next
            
            chain = chain.next

        if t1 != None:
            chain.next = t1
        if t2 != None:
            chain.next = t2
    
        return head.next