def calPoints(ops):
  """
  :type ops: List[str]
  :rtype: int
  """
  score = []
  if len(ops) == 1 and isNumber(ops[-1]):
    return ops[-1]
  
  for op in ops:
    print("temp: ", len(score), " - " , op)
    if isNumber(op):
      score.append(int(op))
    elif op == "+":
      score.append(score[-1] + score[-2])
    elif op == "D":
      score.append(score[-1] * 2)
    elif op == "C":
      score.pop()
  print("Score: ", score)
  return sum(score)

def isNumber(x):
  try:
    int(x)
    return True
  except:
    return False

ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))