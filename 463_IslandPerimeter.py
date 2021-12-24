def islandPerimeter(grid):
  """
  :type grid: List[List[int]]
  :rtype: int
  """
  # perimeter = 0
  # for x in range(len(grid)):
  #   for y in range(len(grid[x])):
  #     if grid[x][y] == 1:
  #       perimeter += 4
  #       if x > 0 and grid[x-1][y] == 1:
  #         perimeter -= 2
  #       if y > 0 and grid[x][y-1] == 1:
  #         perimeter -= 2
  #     print("Tọa độ: (",x,",",y,")",perimeter)
  # return perimeter
  
  """
    Cách 2
  """
  row = len(grid)
  col = len(grid[0])
  perimeter = x = y = 0
  while x != row and y != col:
    if grid[x][y] == 1:
      perimeter += 4
      if x > 0 and grid[x-1][y] == 1:
        perimeter -= 2
      if y > 0 and grid[x][y-1] == 1:
        perimeter -= 2
    if y == col - 1:
      x +=1
      y = 0
    else:
      y += 1
  return perimeter
    
    


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid))