""" score = [[90,80,100,70,80,90,100,90],
	 [60,30,90,90,85,80,75,70],
	 [85,60,99,100,90,80,70,60]]

print(score[0])
print(score[1][2])
print(score[2][0:])
print(len(score[2])) """

score = [[90,80,100,70,80,90,100,90],
	 [60,30,90,90,85,80,75,70],
	 [85,60,99,100,90,80,70,60]]
min = [100]*3
for j in range(3):
	for i in range(8):
		if min[j] > score[j][i]:
			min[j] = score[j][i]
	print("Min = ",min[j])