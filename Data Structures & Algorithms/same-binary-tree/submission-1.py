# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = Queue(), Queue()
        if p is None and q is None:
            return True
        if ((p is None) ^ (q is None)):
            return False
        q1.put(p)
        q2.put(q)
        while q1.empty() == False and q2.empty() == False:
            node1 = q1.get()
            node2 = q2.get()

            if node1.val != node2.val:
                return False
            if (node1.left is None) ^ (node2.left is None):
                return False
            if (node1.right is None) ^ (node2.right is None):
                return False

            if node1.left:
                q1.put(node1.left)
                q2.put(node2.left)
            if node1.right:
                q1.put(node1.right)
                q2.put(node2.right)

        return True
