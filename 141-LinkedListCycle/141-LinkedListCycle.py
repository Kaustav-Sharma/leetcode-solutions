# Last updated: 22/10/2026, 4:43:46 pm
class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle
        