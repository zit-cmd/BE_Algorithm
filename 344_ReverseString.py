def reverseString(s):
  """
  :type s: List[str]
  :rtype: None Do not return anything, modify s in-place instead.
  """
  # ---Cách 1---
  # max_index = len(s) - 1
  # s = [s[max_index - index] for index in range(len(s))]
  # return s
  # ---Cách 2---
  # list[<Start>:<End>:<Step>]
  # return s[::-1]
  # ---Cách 3---
  return s.reverse()

s = ["h","e","l","l","o"]
print(reverseString(s))