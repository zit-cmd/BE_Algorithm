def findLUSlength(a, b):
  """
  :type a: str
  :type b: str
  :rtype: int
  """
  if a == b:
    return -1
  
  return max(len(a), len(b))

print(findLUSlength("asafer","sddqwr"))