# Time Complexity: O(n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        #middle
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        #reverse second half
        prev=None
        curr=slow.next
        slow.next=None
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        #merge
        slow=head
        fast=prev
        
        while(fast):
            temp=slow.next
            slow.next=fast
            fast=fast.next
            slow.next.next=temp
            slow=slow.next.next
        


        

        