# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #print(f"slow is at {slow.val}")

        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # while prev:
        #     print(f"prev is at {prev.val}")
        #     prev = prev.next
        # while head:
        #     print(f"head is at {head.val}")
        #     head = head.next
        
        i, j = head, prev
        while i.next and j.next:
            i_next = i.next
            j_next = j.next
            i.next = j
            j.next = i_next
            i = i_next
            j = j_next
        