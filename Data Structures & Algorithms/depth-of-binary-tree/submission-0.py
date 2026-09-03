# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #bfs approach recursively. find roots

        #base case return 0 (no depth)
        if not root:
            return 0

        #as you go down and find a root then you add 1 on the way up
        #recursively go down left and right respectively then take the larger one
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

