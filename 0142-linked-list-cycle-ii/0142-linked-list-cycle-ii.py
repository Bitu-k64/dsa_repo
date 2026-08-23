class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Cycle detect
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Find starting point
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None