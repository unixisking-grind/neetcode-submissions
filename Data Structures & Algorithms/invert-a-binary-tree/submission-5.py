# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        q = Queue()
        q.put(root)

        while not q.empty():
            currentNode = q.get()

            tmpLeft = None
            tmpRight = None

            if not currentNode:
                continue
            
            tmpLeft = currentNode.left
            tmpRight = currentNode.right

            currentNode.left = tmpRight
            q.put(currentNode.left)

            currentNode.right = tmpLeft
            q.put(currentNode.right)
        return root


        