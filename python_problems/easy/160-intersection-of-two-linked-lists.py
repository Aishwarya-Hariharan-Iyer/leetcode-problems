# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        dictA = dict()
        currA = headA

        while currA:
            dictA[currA] = currA
            currA = currA.next

        currB = headB

        while currB:
            if dictA.get(currB, None): #intersection
                return currB
            currB = currB.next
        
        return None
