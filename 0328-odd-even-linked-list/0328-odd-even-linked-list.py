# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head
        
        odd_node = head
        even_node = head.next
        even_first = even_node
        
        while True:
            if (odd_node == None or even_node == None or even_node.next == None): 
                odd_node.next = even_first 
                break
            
            odd_node.next = even_node.next
            odd_node = even_node.next
            
            if odd_node.next == None: 
                even_node.next = None
                odd_node.next = even_first 
                break
            
            even_node.next = odd_node.next
            even_node = odd_node.next
        
        return head
        