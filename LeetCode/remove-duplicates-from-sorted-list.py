# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        temp = head
        s = set()
        while temp!=None:
            s.add(temp.val)
            temp = temp.next
        s = list(s)
        s.sort()
        dummy = ListNode()
        temp = dummy
        f = 0
        for i in s:
            if f == 0:
                temp.val = i
                f+=1
            else:
                temp.next = ListNode(i)
                temp = temp.next
        return dummy 
