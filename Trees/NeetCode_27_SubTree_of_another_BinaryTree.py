572. Subtree of Another Tree
My solution:
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return (sameTree(root.left, subRoot.left) and 
                        sameTree(root.right, subRoot.right))
            return False 
        
        if not subRoot: 
            return True
        if not root: 
            return False

        if sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
