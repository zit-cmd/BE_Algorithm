# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  def PrintTree(self):
    if self.left:
        self.left.PrintTree()
    print( self.val),
    if self.right:
        self.right.PrintTree()
class Solution(object):
  def mergeTrees(self, root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: TreeNode
    """
    if root1 == None:
      return root2
    if root2 == None:
      return root1
    root1.val += root2.val
    root1.left = self.mergeTrees(root1.left, root2.left)
    root1.right = self.mergeTrees(root1.right, root2.right)
    return root1

root1 = TreeNode(1, TreeNode(3, TreeNode(5), None), TreeNode(2))
root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
root = Solution().mergeTrees(root1, root2)
root.PrintTree()