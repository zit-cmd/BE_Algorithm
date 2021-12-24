# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution(object):
  def averageOfLevels(self, root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    arr = []
    self.average(root, 0 , arr)
    return [ x[0]/x[-1] for x in arr]

  def average(self, root, i, arr):
    if root == None:
      return
    
    if i < len(arr):
      arr[i][0] += root.val
      arr[i][-1] +=1
    else:
      arr.append([root.val * 1.0, 1])
    
    root.left = self.average(root.left, i+1, arr)
    root.right = self.average(root.right, i+1, arr)


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().averageOfLevels(root))