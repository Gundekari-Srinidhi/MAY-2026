# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp=head
        prev=None

        head=head.next
        while temp and temp.next:
            first=temp
            second=temp.next

            first.next=second.next
            second.next=first 

            if prev:
                prev.next=second
            prev=first
            temp=temp.next
        return head