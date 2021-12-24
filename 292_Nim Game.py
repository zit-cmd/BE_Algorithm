def canWinNim(n):
  """
  :type n: int
  :rtype: bool
  """
  """
  n = 4 thì đối thủ sẽ thắng
  => 4*i (i=1,2,3...) thì đối thủ thắng và ngược lại n != 4*i (i=1,2,3,...) thì ta win
  """
  return n % 4 != 0

print(canWinNim(4))