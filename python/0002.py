### 0002. Add Two Numbers ###

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        list_repr = []
        node = self
        while node:
            list_repr.append(node.val)
            node = node.next
        return str(list_repr)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        trace = head
        sum = 0
        while l1 or l2 or sum != 0:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            new_node = ListNode()
            new_node.val = sum % 10
            trace.next = new_node
            trace = new_node
            sum = int(sum / 10)
        return head.next

if __name__ == '__main__':
    solution = Solution()
    list_node_object = []
    head = [ListNode(), ListNode()]
    trace = [head[0], head[1]]
    node_list = [[2,4,3], [5,6,4]]
    for i in range(len(head)):
        for num in node_list[i]:
            new_node = ListNode()
            new_node.val = num
            trace[i].next = new_node
            trace[i] = new_node
        list_node_object.append(head[i].next)
    print(solution.addTwoNumbers(list_node_object[0], list_node_object[1]))
