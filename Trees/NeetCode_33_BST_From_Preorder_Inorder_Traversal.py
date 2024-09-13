105. Construct Binary Tree from Preorder and Inorder Traversal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None 

        root = TreeNode(preorder[0])
        # Part, where to partition the tree 
        mid = inorder.index(preorder[0])

        # Left subtree contains elements starting after root element in the inorder tree. 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
