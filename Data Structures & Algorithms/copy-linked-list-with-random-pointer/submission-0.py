"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    new_nodes = dict()

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = self.recurse(head)
        head = curr
        while curr:
            if curr.random is not None:
                curr.random = self.new_nodes[curr.random]
            curr = curr.next

        return head
    
    def recurse(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # this is essentially creating a deep copy of a graph

        if head.next is None:
            self.new_nodes[head] = Node(head.val, None, head.random)
            return self.new_nodes[head]

        next_node = self.recurse(head.next)
        self.new_nodes[head] = Node(head.val, next_node, head.random)

        return self.new_nodes[head]