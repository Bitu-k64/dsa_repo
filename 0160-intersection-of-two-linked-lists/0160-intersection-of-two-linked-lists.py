# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        # Dono lists ke head se start karo
        p1 = headA
        p2 = headB

        # Jab tak dono same node par nahi milte
        while p1 != p2:

            # A khatam → B ke head par jao
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next

            # B khatam → A ke head par jao
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next

        # Same node intersection point hai
        return p1