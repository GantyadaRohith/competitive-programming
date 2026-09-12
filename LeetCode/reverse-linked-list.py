# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if head == None:
            return head
        elif prev.next == None:
            return head
        elif prev.next.next == None:
            head = prev.next
            head.next = prev
            prev.next = None
            return head
        else:
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev


            
        