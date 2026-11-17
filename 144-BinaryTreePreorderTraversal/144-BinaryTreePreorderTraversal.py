# Last updated: 17/11/2026, 9:28:26 pm
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            if not node:
                return
            
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)

        return res