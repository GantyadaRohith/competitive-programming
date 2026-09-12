# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        if temp is None:
            return head
        if temp.next is None:
            return head
        cnt = 0
        temp = head
        while temp is not None:
            temp = temp.next
            cnt+=1
        k%=cnt
        temp = head
        for i in range(k):
            temp = head
            while temp.next.next is not None:
                temp = temp.next
            temp.next.next = head
            head = temp.next
            temp.next = None
        return head