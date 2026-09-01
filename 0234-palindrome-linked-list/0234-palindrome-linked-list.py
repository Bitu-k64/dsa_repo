# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        new_head = self.reverseList(slow.next)

        first = head
        second = new_head

        while second != None:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        self.reverseList(new_head)

        return True

    # YE FUNCTION ADD KIYA GAYA HAI
    def reverseList(self, head):
        prev = None
        curr = head

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev