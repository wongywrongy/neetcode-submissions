# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both is null then they are same base case
        if not p and not q:
            return True
        
        # take values of the current p and q and they have to be equal
        if p and q and p.val == q.val:
            # iterate down each node on each respective tree at the same time (left and right respectively)
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

        