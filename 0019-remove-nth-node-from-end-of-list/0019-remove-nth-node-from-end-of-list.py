class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head

        # fast ko n steps aage
        for i in range(n):
            fast = fast.next

        # head node delete karna ho
        if fast == None:
            return head.next

        # slow aur fast ko move karo
        while fast.next != None:
            slow = slow.next
            fast = fast.next

        # node delete
        slow.next = slow.next.next

        return head