# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # lowest means the deepest here
        # So basically if p and q are smaller than current val then they will lie to the left
        # if > then to the right
        # if the split then thats the LCA right there
       
        if not root or root == p or root == q:
            return root

        left =  self.lowestCommonAncestor(root.left, p, q)
        right =  self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root

        return left if left else right

        

    

