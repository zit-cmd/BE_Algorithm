def hammingDistance(x, y):
  """
  :type x: int
  :type y: int
  :rtype: int
  """
  count = 0
  while x != 0 or y != 0:
    if x%2 != y%2:
      count+=1
    x//=2
    y//=2
    print(x , y)
  return count
  # return bin(x^y).count("1") 
print(hammingDistance(15,1))