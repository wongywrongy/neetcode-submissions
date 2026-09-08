# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # outer search, visit every node (could subtree start here?)

        # base case cannot have a subtree if it is last node
        if not root:
            return False
        
        # does subroot match starting at this node all the way down?
        if self.sameTree(root, subRoot):
            return True

        # not at current node try left or right 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, a, b):
        # inner check are these trees identical from here

        # if both are nothing then they match 
        if not a and not b:
            return True

        # if one ran out or their values are different
        if not a or not b or a.val != b.val:
            return False

        # return their values and both children must match
        return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)
    