def lengthOfLongestSubstring(s):
  """
  :type s: str
  :rtype: int
  """
  if len(s) == 1: return 1
  temp = ""
  result = 0
  for i in s:
    # if i in temp:
    #   temp = temp[temp.find(i)+1:len(temp)] + i
    # else: 
    #   temp+=i
    #   print(temp)
    temp = temp[temp.find(i)+1:len(temp)] + i if i in temp else temp + i
    # ternary operator
    lenStr = len(temp)
    result = lenStr if lenStr > result else result

  return result

print(lengthOfLongestSubstring("dvdf"))