# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        # Step 1
        dummy = ListNode(0, head)

        # Step 2
        prev = dummy
        curr = head

        # Step 3
        while curr and curr.next:
            next_pair = curr.next.next
            second = curr.next
            second.next = curr
            curr.next = next_pair
            prev.next = second
            prev = curr
            curr = next_pair
        
        return dummy.next