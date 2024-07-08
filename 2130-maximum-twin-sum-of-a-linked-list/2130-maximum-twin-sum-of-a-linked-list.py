# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        curr_node = head
        
        while curr_node:
            next_node = curr_node.next
            curr_node.next = dummy_node.next
            dummy_node.next = curr_node
            curr_node = next_node
            
        return dummy_node.next
        
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 중간 점 찾기
        slow_pointer, fast_pointer = head, head.next
        
        while fast_pointer and fast_pointer.next:
            slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
        
        
        pa = head
        q = slow_pointer.next
        slow_pointer.next = None 
        # 중간점을 기준으로 reverse
        pb = self.reverseNode(q)

        ans = 0
        while pa and pb:
            ans = max(ans, pa.val + pb.val)
            pa = pa.next
            pb = pb.next
            
        return ans