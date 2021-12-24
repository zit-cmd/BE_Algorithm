def matrixReshape(mat, r, c):
  """
  :type mat: List[List[int]]
  :type r: int
  :type c: int
  :rtype: List[List[int]]
  """
  rMat = len(mat)
  cMat = len(mat[0])
  if r >= rMat and c >= cMat or r*c != rMat*cMat:
    return mat
  newMat = [[]]
  x = i = k = 0
  # for i in range(rMat):
  #   for k in range(cMat):
  #     # print("Mat: ", newMat, " r: ", len(newMat)," c: ", len(newMat[x]))
  #     if len(newMat[x]) == c:
  #       x+=1
  #       newMat.append([])
  #     # print("Mat: ", newMat, " r: ", len(newMat)," c: ", len(newMat[x]))
  #     newMat[x].append(mat[i][k])
  
  # dùng while
  while r!=x:
    newMat[x].append(mat[i][k])
    # print("Mat: ", newMat, " r: ", len(newMat)," c: ", len(newMat[x]))
    if k == cMat-1:
      k=0
      i+=1
    else: k+=1
    # print("Mat: ", newMat, " r: ", len(newMat)," c: ", len(newMat[x]), "k: ", k, "i", i)
    if i == rMat:
      break
    if len(newMat[x]) == c:
      x+=1
      newMat.append([])
  return newMat

      
mat = [[1,2]]
r = 1
c = 1

print(matrixReshape(mat, r, c))