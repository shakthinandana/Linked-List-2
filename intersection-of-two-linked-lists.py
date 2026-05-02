# Time Complexity: O(m+n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """        
        lenA=0
        lenB=0
        p1,p2=headA,headB
        while(p1):
            p1=p1.next
            lenA+=1
        while(p2):
            p2=p2.next
            lenB+=1

        p1=headA
        p2=headB
        while(lenA>lenB):
            p1=p1.next
            lenA-=1
        while(lenB>lenA):
            p2=p2.next
            lenB-=1
        
        while(p1 and p2):
            if p1==p2:
                return p1
            p1=p1.next
            p2=p2.next
        return None