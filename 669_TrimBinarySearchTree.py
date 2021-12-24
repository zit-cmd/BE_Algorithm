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
  def trimBST(self, root, low, high):
    """
    :type root: TreeNode
    :type low: int
    :type high: int
    :rtype: TreeNode
    Note: Node cần 2 điều kiện node đó phải lớn hơn các con bên trái và nhỏ hơn các con bên phải
    """
    if root == None:
      return

    if root.val < low:
      root = root.right
      return self.trimBST(root, low, high)
    elif root.val > high:
      root = root.left
      return self.trimBST(root, low, high)

    root.left = self.trimBST(root.left, low, high)
    root.right = self.trimBST(root.right, low, high)

    return root

root = TreeNode(1, TreeNode(0), TreeNode(2))
root = Solution().trimBST(root, 1, 2)
root.PrintTree()