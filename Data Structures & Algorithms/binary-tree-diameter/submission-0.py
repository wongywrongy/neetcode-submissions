# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # make a level number

        # dfs approach

        # as long as the left or right is not null then recursion

        # while left or right != null
            # recursively go down left and right
                # on the way down every time we go down a level +1 number

            # take the max value from either the left or right path

        # return that max level number


        self.max_diameter = 0

        def dfs(node):
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.max_diameter = max(
                self.max_diameter,
                left_height + right_height
            )

            return 1 + max(left_height, right_height)

        dfs(root)

        return self.max_diameter