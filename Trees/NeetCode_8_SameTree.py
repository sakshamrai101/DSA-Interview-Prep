100. Same Tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Empty Trees
        if not p and not q:
            return True
        #Either one tree is empty or the value of root node is not same. 
        if not p or not q or p.val != q.val:
            return False 
        
        # Recursive traversal step. 
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
