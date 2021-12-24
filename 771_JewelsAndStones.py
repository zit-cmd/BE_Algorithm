def numJewelsInStones(jewels, stones):
  """
  :type jewels: str
  :type stones: str
  :rtype: int
  """
  # Challenge: Could you write the code in one line?
  """
    String method: str.count(sub, start= 0,end=len(string))
  """
  # return  sum([stones.count(i) for i in jewels])
  """
  for biến stones và kiểm tra từng item có trong biến jewels 
  => ta được 1 list item có trong jewels => len(<list>)
  """
  return len([i for i in stones if i in jewels])

print(numJewelsInStones("z", "ZZ"))