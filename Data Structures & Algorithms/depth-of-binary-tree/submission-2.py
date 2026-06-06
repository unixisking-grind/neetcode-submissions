# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node: Optional[TreeNode], depth: int, m: int):
            if not node:
                return m
            if depth > m:
                m = depth
            return max(
                dfs(node.left, depth + 1, m),
                dfs(node.right, depth + 1, m)
            )
        return dfs(root, 1, 1)