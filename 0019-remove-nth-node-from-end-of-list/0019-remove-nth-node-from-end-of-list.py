# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        while temp:
            temp=temp.next
            length+=1
        flag=head
        if n==length:
            return head.next
        for i in range(length-n-1):
            flag=flag.next
        if flag.next:
            flag.next=flag.next.next
        return head



        