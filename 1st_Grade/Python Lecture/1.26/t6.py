score = [[90, 80, 100, 70, 80, 90, 100, 90],
 [60, 30, 90, 90, 85, 80, 75, 70],
  [85, 60, 99, 100, 90, 80, 70, 60]]
for i in range(len(score)):
    min = score[i][0]
    for j in range(len(score[i])):
        if min> score[i][j]:
            min = score[i][j] 
    print("Min[%d] = %d" %(i,min))
