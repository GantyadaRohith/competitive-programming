# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=1
        dummy=ListNode(0,head)
        temp=dummy
        while temp.next:
            c+=1
            temp=temp.next
        pos=c-n-1
        temp=dummy
        for _ in range(pos):
            temp=temp.next
        temp.next=temp.next.next
        return dummy.next