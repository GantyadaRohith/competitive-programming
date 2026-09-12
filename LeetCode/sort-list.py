# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergesort(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = mergesort(left)
            right = mergesort(right)
            return merge(left, right)

        def split(head):
            # Use fast = head.next so slow stops at the end of left half
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        def merge(l, r):
            dummy = tail = ListNode()
            while l and r:
                if l.val < r.val:
                    tail.next = l
                    l = l.next
                else:
                    tail.next = r
                    r = r.next
                tail = tail.next
            tail.next = l or r
            return dummy.next

        return mergesort(head)
