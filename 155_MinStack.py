class MinStack(object):

  def __init__(self):
    self.val = []  
    self.min = []

  def push(self, val):
    """
    :type val: int
    :rtype: None
    """
    self.val.append(val)
    if not self.min or self.min[-1] >= val:
      self.min.append(val)
    # Tham khảo:
    # minimum = val
    # if self.val and self.val[-1][1] < minimum:
    #     minimum = self.val[-1][1]
    # self.val.append([val, minimum])

  def pop(self):
    """
    :rtype: None
    """
    if self.top() == self.min[-1]:
      self.min.pop()
    self.val.pop()

  def top(self):
    """
    :rtype: int
    """
    return self.val[-1]  

  def getMin(self):
    """
    :rtype: int
    """
    print(self.min)
    return self.min[-1]
  
  def outputStack(self):
    for i in self.val:
      print(i)

minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
# print("Stack: ")
# minStack.outputStack()
print("Min: ", minStack.getMin()) # return -3
minStack.pop()
print("Top: ", minStack.top())   # return 0
print("Min: ", minStack.getMin()) # return -2