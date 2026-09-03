# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursively call if not bottomnost leaf then dont return anything
        if not root: 
            return None

        #from the root swap the left and right trees recursively (so it goes downwrd)
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        #return the bottommost root as it goes up should be in tree order
        return root
