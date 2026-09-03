# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #bfs approach
        #count by levels

        #base case
        if not root:
            return 0

        best = 0
        #node and its depth
        stack = [(root,1)]

        #the moment you take a child you add +1 to depth
        #as you go append to a stack 
        while stack:
            node,d = stack.pop()
            best = max(best,d)

            if node.left:
                stack.append((node.left, d+1))
            if node.right:
                stack.append((node.right,d+1))

        return best 