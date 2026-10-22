# Last updated: 22/10/2026, 4:44:00 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        a= []
        for linked_list in lists:
            while linked_list:
                a.append(linked_list.val)
                linked_list = linked_list.next
        a.sort()
        d = ListNode()
        current = d
        for val in a:
            current.next = ListNode(val)
            current = current.next
        return d.next