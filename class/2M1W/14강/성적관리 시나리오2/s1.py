score =[0]*8

ts = [('T',90 ,60, 85),
('P', 80, 30, 60),
('O', 100, 90, 99),
('X', 70, 90, 100),
('M', 80, 85, 90),
('Ma', 90, 80, 90),
('Me', 100, 75, 70),
('Ab', 90, 70, 60 )]

total_s = [0]*8

for j in range(8):
    total = 0
    
    total += int(ts[j][1])*0.1
    total += int(ts[j][2])*0.3
    total += int(ts[j][3])*0.6
    
    total_s[j] = (ts[j][0],int(total))


ft = open('score1.txt','w')
for i in range(8):
    ft.write(str(total_s[i][0]))
    ft.write(":")
    ft.write(str(total_s[i][1]))
    ft.write('\n')
    
    
ft.close()
