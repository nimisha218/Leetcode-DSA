# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Find the middle of the Linked List first
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # print("Middle: ", slow.val)

        second_list = slow
        # Let's reverse the second list

        prev = None
        curr = second_list

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # print("First half: ", head)
        # print("Reversed second half: ", prev)

        ans = 0
        while prev:
            ans = max(ans, prev.val + head.val)
            head = head.next
            prev = prev.next

        return ans