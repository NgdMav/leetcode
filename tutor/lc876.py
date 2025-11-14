# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 1
        current = head
        while current.next != None:
            size += 1
            current = current.next
        current = head
        size = size // 2 + 1
        for i in range(1, size):
            current = current.next
        return current