# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #the property of a binary tree is that all the left nodes are < right nodes
        #the inverse would just make it so the right nodes now are < the left nodes 

        #we're going to need a temp
        #we're also going to need to traverse this tree breadth-wise 
        #we have to touch every node

        if not root:
            return None
        
        temp = root.left

        root.left = root.right
        root.right =  temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 
