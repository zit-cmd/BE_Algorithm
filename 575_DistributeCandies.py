def distributeCandies(candyType):
  """
  :type candyType: List[int]
  :rtype: int
  """
  # arr = []
  # for i in candyType:
  #   if len(arr) == len(candyType)/2: 
  #     return len(arr)
  #   if i not in arr:
  #     arr.append(i)
  # return len(arr)
  return min(len(candyType)/2, len(set(candyType)))

print(distributeCandies([6,6,6,2]))